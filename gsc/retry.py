import time
import functools
from typing import Callable, TypeVar

from googleapiclient.errors import HttpError

T = TypeVar("T")

_RETRYABLE_STATUS = {429, 500, 502, 503, 504}
_MAX_RETRIES = 5
_BASE_DELAY = 1.0  # seconds


def with_retry(fn: Callable[..., T], *args, **kwargs) -> T:
    """
    Call fn(*args, **kwargs) with exponential backoff on retryable HTTP errors.
    Retryable: 429 (rate limit), 500/502/503/504 (transient server errors).
    Non-retryable errors propagate immediately.
    """
    delay = _BASE_DELAY
    for attempt in range(_MAX_RETRIES):
        try:
            return fn(*args, **kwargs)
        except HttpError as e:
            status = e.resp.status if hasattr(e, "resp") else 0
            if status not in _RETRYABLE_STATUS or attempt == _MAX_RETRIES - 1:
                # Non-retryable or exhausted — raise a clean message
                raise _clean_http_error(e) from None
            time.sleep(delay)
            delay = min(delay * 2, 60)  # cap at 60s
    # unreachable, but satisfies type checkers
    raise RuntimeError("retry loop exited unexpectedly")


def _clean_http_error(e: HttpError) -> Exception:
    status = e.resp.status if hasattr(e, "resp") else "?"
    reason = _extract_reason(e)
    messages = {
        400: f"Bad request — {reason}",
        401: "Authentication failed. Run reauthenticate() for this account.",
        403: f"Access denied — {reason}. Check that this account has access to the GSC property.",
        404: (
            "Property not found. Use list_properties() to see available properties. "
            "Domain properties must be prefixed with 'sc-domain:' (e.g. sc-domain:example.com)."
        ),
        429: "GSC API rate limit hit after retries. Wait a few minutes and try again.",
        500: "GSC API returned a server error. Try again shortly.",
        503: "GSC API is temporarily unavailable. Try again shortly.",
    }
    msg = messages.get(status, f"GSC API error {status}: {reason}")
    return RuntimeError(msg)


def _extract_reason(e: HttpError) -> str:
    try:
        import json
        content = json.loads(e.content)
        error = content.get("error", {})
        return error.get("message", str(e))
    except Exception:
        return str(e)


def retryable(fn):
    """Decorator: wrap a function so all internal HttpErrors use with_retry semantics."""
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        return with_retry(fn, *args, **kwargs)
    return wrapper
