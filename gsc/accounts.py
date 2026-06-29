import json
import os
from pathlib import Path
from typing import Optional

from googleapiclient.discovery import build

from gsc.auth.oauth import get_oauth_credentials
from gsc.auth.service_account import get_service_account_credentials

_DEFAULT_CONFIG_PATH = os.environ.get(
    "GSC_ACCOUNTS_CONFIG", os.path.expanduser("~/.config/mcp-search-console/accounts.json")
)


class AccountError(Exception):
    pass


class AccountManager:
    def __init__(self, config_path: str = _DEFAULT_CONFIG_PATH):
        self._config_path = config_path
        self._config = self._load_config()
        # Cache: account_name -> authenticated GSC service resource
        self._clients: dict[str, object] = {}

    def _load_config(self) -> dict:
        path = Path(self._config_path)
        if not path.exists():
            raise AccountError(
                f"Accounts config not found at {self._config_path}. "
                "Copy accounts.example.json and set GSC_ACCOUNTS_CONFIG."
            )
        with path.open() as f:
            return json.load(f)

    def _resolve_account(self, account: Optional[str]) -> str:
        name = account or self._config.get("default")
        if not name:
            raise AccountError("No account specified and no default set in config.")
        if name not in self._config.get("accounts", {}):
            raise AccountError(
                f"Account '{name}' not found in config. "
                f"Available: {', '.join(self._config['accounts'].keys())}"
            )
        return name

    def get_client(self, account: Optional[str] = None):
        name = self._resolve_account(account)

        if name not in self._clients:
            self._clients[name] = self._build_client(name)

        # Re-validate credentials are still fresh on each access
        client = self._clients[name]
        creds = client._http.credentials
        if hasattr(creds, "expired") and creds.expired:
            # Force refresh and rebuild
            del self._clients[name]
            self._clients[name] = self._build_client(name)

        return self._clients[name]

    def _build_client(self, name: str):
        cfg = self._config["accounts"][name]
        auth_type = cfg.get("type", "oauth")

        if auth_type == "oauth":
            creds = get_oauth_credentials(
                client_secrets_file=cfg["client_secrets_file"],
                token_file=cfg["token_file"],
            )
        elif auth_type == "service_account":
            creds = get_service_account_credentials(cfg["credentials_file"])
        else:
            raise AccountError(f"Unknown auth type '{auth_type}' for account '{name}'.")

        return build("webmasters", "v3", credentials=creds, cache_discovery=False)

    def list_accounts(self) -> list[dict]:
        default = self._config.get("default")
        result = []
        for name, cfg in self._config.get("accounts", {}).items():
            result.append(
                {
                    "name": name,
                    "type": cfg.get("type", "oauth"),
                    "is_default": name == default,
                    "authenticated": name in self._clients,
                }
            )
        return result

    def set_default(self, account: str) -> None:
        if account not in self._config.get("accounts", {}):
            raise AccountError(
                f"Account '{account}' not found. "
                f"Available: {', '.join(self._config['accounts'].keys())}"
            )
        self._config["default"] = account
        # Persist the change
        with open(self._config_path, "w") as f:
            json.dump(self._config, f, indent=2)

    def invalidate(self, account: Optional[str] = None) -> None:
        """Force re-authentication for an account (clears cached client)."""
        name = self._resolve_account(account)
        self._clients.pop(name, None)
        # Also delete the token file so OAuth re-runs the flow
        cfg = self._config["accounts"][name]
        if cfg.get("type") == "oauth" and "token_file" in cfg:
            token_path = Path(os.path.expanduser(cfg["token_file"]))
            if token_path.exists():
                token_path.unlink()
