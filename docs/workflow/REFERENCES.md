# Search Console multi-account MCP: source and knowledge custody

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | Current main candidate 7b77d88 is the 2026-09-16 CI-gate merge. |
| **Where?** | README.md, pyproject.toml, gsc/server.py. |
| **Why it exists?** | Search Console multi-account MCP needs this document to retain source lineage and freshness without promoting retrieved content to authority. |
| **Why this approach?** | Current main candidate 7b77d88 is the 2026-09-16 CI-gate merge. |
| **Why it matters?** | Canonical source changes must not silently leave a trusted-looking stale knowledge copy. |

## Canonical source register

The following local sources support this dossier. They were read directly or inspected through relevant excerpts and handler/test definitions on 2026-09-26. The evidence inventory records hashes, not a claim that every line has received an exhaustive audit. Original manuals/specifications retain their history; these documents summarize current behavior and explicit gaps. Git commit messages provide chronology, not a substitute for inspecting implementation.

- [README.md](../../README.md)
- [pyproject.toml](../../pyproject.toml)
- [gsc/server.py](../../gsc/server.py)
- [gsc/accounts.py](../../gsc/accounts.py)
- [gsc/auth/oauth.py](../../gsc/auth/oauth.py)
- [gsc/auth/service_account.py](../../gsc/auth/service_account.py)
- [gsc/retry.py](../../gsc/retry.py)
- [tests/test_server.py](../../tests/test_server.py)

## Knowledge update events

After a material requirement, interface, decision, verified outcome, source relocation or task-state change, update the owning canonical document first. Record an event containing changed source/revision, decision or evidence, intended knowledge target, rights/sensitivity, freshness state and required readback. Only update a target already bound and authorized for that scope. Record the exact resulting source/version and a bounded readback; if access or permission is missing, retain a pending event rather than claim synchronization. Revalidate on source drift, not just elapsed time.

QMD is scoped local retrieval; NotebookLM is a separate provider corpus; the personal Brain is a separate curated knowledge system. None is source authority. No verified project-specific remote notebook or personal-Brain write binding was established in this reconstruction. Do not choose one by a matching name or bulk-upload source code/customer records. No external knowledge write or retrieval of private corpus contents occurred.


## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
