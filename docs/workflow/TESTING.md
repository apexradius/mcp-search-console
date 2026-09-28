# Search Console multi-account MCP: acceptance evidence

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | tests/test_server.py asserts all 17 schemas, missing config, ten-URL guards, sitemap denial without an environment flag and retry pass-through/non-HTTP behavior. |
| **Where?** | tests/test_server.py. |
| **Why it exists?** | Search Console multi-account MCP needs this document to choose a check that proves the changed behavior without claiming broader evidence. |
| **Why this approach?** | tests/test_server.py asserts all 17 schemas, missing config, ten-URL guards, sitemap denial without an environment flag and retry pass-through/non-HTTP behavior. |
| **Why it matters?** | A registration or document check cannot prove live authentication, provider state or the installed user path. |

## Required proof by behavior

tests/test_server.py asserts all 17 schemas, missing config, ten-URL guards, sitemap denial without an environment flag and retry pass-through/non-HTTP behavior. Those mocked tests neither authorize writes nor demonstrate real OAuth, GSC quotas, indexing or current analytics. For a code change use python -m unittest discover -s tests in the verified existing environment, and add fake-service request-body tests for the changed endpoint.

## Product acceptance baseline

Resolve named OAuth/service-account profiles without restarting the server. Expose the 17 current tools with explicit property scope and bounded URL inspection. Return understandable authorization/rate-limit errors. Sitemap submission and deletion must be treated as external writes even though they sit beside read tools. Never turn analytics absence into a guaranteed absence of traffic or a live-page diagnosis.

## Evidence custody

Inspected means source/test definitions were read. Locally verified means the named executable check actually ran and its result was observed. Live verified requires the deployed, installed or user-facing path. Historical checkmarks and CI configuration are not fresh results. Use the exact candidate, environment, test input class, observed result and limitations in a receipt. Read [AGENTS](AGENTS.md) for conditional AXI/crew custody; do not create a pipeline merely because this file exists.

## Supporting sources

- [tests/test_server.py](../../tests/test_server.py)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.

## Document checker setup

The navigation checks use CommonMark parsing to distinguish rendered links from code examples. In a Python virtual environment, install the pinned validation dependencies with `python -m pip install -r tools/requirements-workflow.txt` before running the document checkers and their fixtures. CI installs the same pins.
