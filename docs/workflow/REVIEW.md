# Search Console MCP: documentation review continuity

Observed 2026-09-28 against source baseline `7b77d888e71197486a67815d3462f66c80c2036f`. This is a bounded continuity check of the earlier independent source review, not a new runtime or product acceptance test.

The 8 primary-source hashes recorded in the prior review still match this candidate baseline. The project-specific role bodies are retained; this change adds portable navigation, an actual-source map, a domain glossary and executable document checks. Historical/local-only references remain explicitly unavailable rather than being invented or silently imported.

## Previously source-challenged scenarios

### Recover an implicit OAuth profile after401

Reader recovery: Dossier originally overpromised token deletion. Corrected docs distinguish always-cleared client cache, explicit-type token unlink and omitted-type OAuth construction; fresh consent is not guaranteed. No credentials opened.

Source and dossier evidence: ["gsc/accounts.py", "gsc/server.py:reauthenticate", "gsc/auth/oauth.py", "docs/workflow/DATABASE.md", "docs/workflow/API.md"]

Result: pass_after_document_correction

Evidence level: inspected

### Use GSC_ALLOW_DESTRUCTIVE=false and inspect eleven URLs before a sitemap update

Reader recovery: Nonempty false still enables both sitemap write guards, independently of actual approval. Batch handlers reject>10 locally; this is not a verified provider-wide limit. Preserve exact property/profile and split authorized reads; submission never proves indexing.

Source and dossier evidence: ["gsc/server.py:submit_sitemap", "gsc/server.py:delete_sitemap", "gsc/server.py:batch_inspect_urls", "gsc/server.py:check_indexing_issues", "docs/workflow/API.md", "prompt.md"]

Result: pass

Evidence level: inspected

## Source binding

| Source | SHA256 |
| --- | --- |
| `README.md` | `74ce3f559f36d964642460696b2fddd831a0ebaf19e3e8d40215ab80a28672ab` |
| `pyproject.toml` | `f1a1a6e15f163b22e2def394c5a118e4c1f4b40c8e3ea522280456bc551b3770` |
| `gsc/server.py` | `69a7fecec1703623a195bb86b3efc428d9062c06d3586a9143731ebcb8e82721` |
| `gsc/accounts.py` | `8a20167c64b438400dd56c69a04a5facbdf46bde32ab124b1cecd8c65f3e326c` |
| `gsc/auth/oauth.py` | `0c52b38596b5b912aac4cfbf90a98ee23ee16b9462cc910535edbbdc58d9575f` |
| `gsc/auth/service_account.py` | `3cacb4dcb6c378d61bdd02ca5472da25eb4a813213e2457e2fc652222799f109` |
| `gsc/retry.py` | `f5e1fbd91298a97d57cd8473b497964ecee8aad23290cf0c29ce7eedccd8eb8d` |
| `tests/test_server.py` | `96946da58f28c88a6682c6fc122ef92d8f6940e311669289537c28fb24a495fb` |

Prior review artifact names: `tooling-independent-review.json`. The owner retains these in the dated 2026-09-26 reconstruction evidence directory. A fresh clone can inspect the above source and scenarios without that private directory.

## Limits

No new fresh-runtime comprehension, deployed behavior, provider operation or release is claimed. The current user request selects work; these scenarios are examples, not standing tasks. Local/CI/merge/knowledge status is recorded separately in review.json.
