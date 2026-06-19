from datetime import datetime, timedelta
from typing import List, Optional

from sqlalchemy.orm import Session

from app.models import Book, Loan, LoanStatus, Member, MemberStatus


class MemberRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, email: str, name: str) -> Member:
        member = Member(email=email, name=name, status=MemberStatus.ACTIVE)
        self.db.add(member)
        self.db.commit()
        self.db.refresh(member)
        return member

    def get(self, member_id: int) -> Optional[Member]:
        return self.db.get(Member, member_id)

    def list_all(self) -> List[Member]:
        return self.db.query(Member).all()


class BookRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, isbn: str, title: str, author: str) -> Book:
        book = Book(isbn=isbn, title=title, author=author)
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def get(self, book_id: int) -> Optional[Book]:
        return self.db.get(Book, book_id)

    def list_all(self) -> List[Book]:
        return self.db.query(Book).all()


class LoanService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_loan(self, member_id: int, book_id: int, days: int) -> Loan:
        member = self.db.get(Member, member_id)
        book = self.db.get(Book, book_id)
        if not member or not book:
            raise ValueError("Member or book not found")
        if member.status != MemberStatus.ACTIVE:
            raise ValueError("Member is not active")

        loan = Loan(
            member_id=member_id,
            book_id=book_id,
            due_at=datetime.utcnow() + timedelta(days=days),
            status=LoanStatus.OPEN,
        )
        self.db.add(loan)
        self.db.commit()
        self.db.refresh(loan)
        return loan

    def list_open_loans(self) -> List[Loan]:
        return self.db.query(Loan).filter(Loan.status == LoanStatus.OPEN).all()

    def mark_overdue(self) -> int:
        now = datetime.utcnow()
        # BUG (I6): inverted comparison — selects loans not yet due instead of past-due
        overdue = (
            self.db.query(Loan)
            .filter(Loan.status == LoanStatus.OPEN, Loan.due_at >= now)
            .all()
        )
        for loan in overdue:
            loan.status = LoanStatus.OVERDUE
        self.db.commit()
        return len(overdue)
