"""Hermetic tests for the Google Search Console MCP server.

No network calls and no real Google credentials are used. These cover the tool
contract, the missing-config path, the batch-size guards, the destructive-op
gate, and the retry wrapper's pass-through behaviour.
"""

import asyncio
import unittest
from unittest import mock

from gsc import server
from gsc.accounts import AccountError, AccountManager
from gsc.retry import with_retry

EXPECTED_TOOLS = {
    "list_accounts",
    "set_default_account",
    "reauthenticate",
    "list_properties",
    "get_site_details",
    "get_search_analytics",
    "get_performance_overview",
    "compare_periods",
    "get_advanced_search_analytics",
    "get_search_by_page",
    "inspect_url",
    "batch_inspect_urls",
    "check_indexing_issues",
    "list_sitemaps",
    "get_sitemap",
    "submit_sitemap",
    "delete_sitemap",
}


class ToolRegistrationTests(unittest.TestCase):
    def test_server_exposes_expected_tools_with_schemas(self):
        tools = asyncio.run(server.mcp.list_tools())
        names = {t.name for t in tools}
        self.assertEqual(names, EXPECTED_TOOLS)
        for t in tools:
            self.assertIsInstance(t.parameters, dict, f"{t.name} has no schema")
            self.assertIn("properties", t.parameters, f"{t.name} schema missing properties")


class ConfigValidationTests(unittest.TestCase):
    def test_missing_config_raises_account_error(self):
        with self.assertRaises(AccountError) as ctx:
            AccountManager(config_path="/nonexistent/path/accounts.json")
        self.assertIn("not found", str(ctx.exception))


class BatchGuardTests(unittest.TestCase):
    def test_batch_inspect_rejects_over_ten_urls(self):
        urls = [f"https://example.com/p{i}" for i in range(11)]
        result = server.batch_inspect_urls("https://example.com", urls)
        self.assertEqual(len(result), 1)
        self.assertIn("Maximum 10", result[0]["error"])

    def test_check_indexing_rejects_over_ten_urls(self):
        urls = [f"https://example.com/p{i}" for i in range(11)]
        result = server.check_indexing_issues("https://example.com", urls)
        self.assertEqual(len(result), 1)
        self.assertIn("Maximum 10", result[0]["error"])


class DestructiveGuardTests(unittest.TestCase):
    def test_submit_sitemap_disabled_without_flag(self):
        with mock.patch.dict("os.environ", {}, clear=True):
            result = server.submit_sitemap("https://example.com", "sitemap.xml")
        self.assertIn("error", result)
        self.assertIn("disabled", result["error"])

    def test_delete_sitemap_disabled_without_flag(self):
        with mock.patch.dict("os.environ", {}, clear=True):
            result = server.delete_sitemap("https://example.com", "sitemap.xml")
        self.assertIn("error", result)
        self.assertIn("disabled", result["error"])


class RetryTests(unittest.TestCase):
    def test_returns_value_on_success(self):
        self.assertEqual(with_retry(lambda: 42), 42)

    def test_non_http_error_propagates_immediately(self):
        def boom():
            raise ValueError("not retryable")

        with self.assertRaises(ValueError):
            with_retry(boom)


if __name__ == "__main__":
    unittest.main()
