# Sample Repo — Library API

An **unfamiliar repo** for repo-discovery and intermediate tasks (B1–B3, I1–I3, I6).

## Stack

- FastAPI + SQLAlchemy (SQLite)
- Cron job: `jobs/overdue_cron.py`
- Tests: pytest + httpx TestClient

## Install & run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Test command

```bash
pytest -v
```

## Task briefs

| Task | What to produce |
|------|-----------------|
| **B1** | Class/service/module inventory (30 min) |
| **B2** | API endpoint map — all `/api/v1/*` routes (30 min) |
| **B3** | Test framework, files, commands, actual output (15 min) |
| **I1** | ER diagram with source file citations (45 min) |
| **I2** | End-to-end flow trace for `POST /api/v1/loans` (45 min) |
| **I3** | Small safe change + test in an unfamiliar module (60 min) |
| **I6** | Diagnose seeded bug — see [BUG_I6.md](BUG_I6.md) (60 min) |

## Hints (do not read until you try)

- Models: `app/models.py`
- Repositories: `app/repositories.py`
- Routes: `app/main.py`
- Cron: `jobs/overdue_cron.py`
