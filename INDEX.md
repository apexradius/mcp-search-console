# Search Console MCP: project index

Start at [prompt.md](prompt.md) for the enduring mission and accepted direction. This index locates the existing project contracts; it does not authorize historical operations.

## Mandatory context

Read applicable repository instructions, [working rules](docs/workflow/AGENTS.md), [current handoff](docs/workflow/HANDOFFS.md), [verification](docs/workflow/TESTING.md) and [knowledge bindings](docs/workflow/REFERENCES.md). Read the relevant source before changing it.

## Task routes

| Requested work | Owning contracts |
| --- | --- |
| Scope, requirements or priorities | [PRD](docs/workflow/PRD.md), [capabilities](docs/workflow/CAPABILITIES.md), [architecture](docs/workflow/ARCHITECTURE.md) |
| Component behavior or bug | [architecture](docs/workflow/ARCHITECTURE.md), [code style](docs/workflow/CODE_STYLE.md), [testing](docs/workflow/TESTING.md) |
| Interface or persistence | [API](docs/workflow/API.md), [database](docs/workflow/DATABASE.md), [security](docs/workflow/SECURITY.md) |
| Visible experience | [design](docs/workflow/DESIGN.md), [wireframes](docs/workflow/WIREFRAMES.md), [PRD](docs/workflow/PRD.md) |
| Configuration, operation or recovery | [security](docs/workflow/SECURITY.md), [secret locations](docs/workflow/SECRETS.md), [maintenance](docs/workflow/MAINTENANCE.md) |
| Resume or close a task | [handoff](docs/workflow/HANDOFFS.md), [report](docs/workflow/REPORT.md), [references](docs/workflow/REFERENCES.md) |

Combine all applicable routes; a security, data or release boundary adds its route even for a small UI edit. Non-applicable roles retain their stated reasons.

## Project source map

| Source | Context owner |
| --- | --- |
| [gsc/server.py](gsc/server.py) | [ARCHITECTURE](docs/workflow/ARCHITECTURE.md) explains its project role |
| [tests/test_server.py](tests/test_server.py) | [ARCHITECTURE](docs/workflow/ARCHITECTURE.md) explains its project role |
| [The root README](README.md) | [README](docs/workflow/README.md) explains its project role |
| [pyproject.toml](pyproject.toml) | [README](docs/workflow/README.md) explains its project role |
| [gsc/accounts.py](gsc/accounts.py) | [DATABASE](docs/workflow/DATABASE.md) explains its project role |

## Domain glossary

| Term | Meaning in this project |
| --- | --- |
| Profile | Credential selection independent of the target property. |
| site_url | Explicit Search Console property target. |
| Cached client | In-process authentication object; not proof of current live access. |

Definitions follow [ARCHITECTURE](docs/workflow/ARCHITECTURE.md); consult that owner for contracts and limitations.

## Review evidence

[Source-bound review continuity](docs/workflow/REVIEW.md) records scenario scope and limits.

## Completion

Use the latest user task and preserve unrelated work. Update affected facts and record verification and continuation. Navigation checks establish neither product readiness nor delivery or knowledge freshness.
