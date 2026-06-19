"""Daily cron job: mark overdue loans."""

import logging

from app.models import SessionLocal, init_db
from app.repositories import LoanService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_overdue_check() -> int:
    init_db()
    db = SessionLocal()
    try:
        service = LoanService(db)
        count = service.mark_overdue()
        logger.info("Marked %s loans as overdue", count)
        return count
    finally:
        db.close()


if __name__ == "__main__":
    run_overdue_check()
