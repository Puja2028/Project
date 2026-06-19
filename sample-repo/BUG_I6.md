# I6 — Seeded Bug (do not read until you attempt reproduction)

There is a subtle bug in the overdue-loan cron path. When loans pass their due date, they may **not** be marked `OVERDUE` as expected.

## Your task

1. Reproduce the issue with a test or manual steps.
2. Identify root cause with file paths.
3. Apply a minimal fix.
4. Run verification (`pytest -v`).
5. Document what the agent suggested vs what you verified.

## Hint

Start by reading `jobs/overdue_cron.py` and tracing into `LoanService.mark_overdue()` in `app/repositories.py`. Pay attention to datetime comparisons.
