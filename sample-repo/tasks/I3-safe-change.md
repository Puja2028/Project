# I3 — Small Safe Change (60 min)

**Goal:** Make a small, focused change in an unfamiliar module; keep diff minimal; add or update a test.

## Suggested change

Add `GET /api/v1/members` that returns a list of all members.

## Required output

- Diff or branch
- Files changed and why
- Test command and result
- Risk assessment
- Agent suggested vs manually verified

## Verification

```bash
cd sample-repo && pytest -v
```
