from datetime import datetime
from enum import Enum

from sqlalchemy import Column, DateTime, Enum as SAEnum, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker

from app.config import DATABASE_URL


class Base(DeclarativeBase):
    pass


class MemberStatus(str, Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"


class LoanStatus(str, Enum):
    OPEN = "open"
    RETURNED = "returned"
    OVERDUE = "overdue"


class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(120), nullable=False)
    status = Column(SAEnum(MemberStatus), default=MemberStatus.ACTIVE)
    created_at = Column(DateTime, default=datetime.utcnow)

    loans = relationship("Loan", back_populates="member")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    isbn = Column(String(20), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    author = Column(String(120), nullable=False)

    loans = relationship("Loan", back_populates="book")


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey("members.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    loaned_at = Column(DateTime, default=datetime.utcnow)
    due_at = Column(DateTime, nullable=False)
    returned_at = Column(DateTime, nullable=True)
    status = Column(SAEnum(LoanStatus), default=LoanStatus.OPEN)

    member = relationship("Member", back_populates="loans")
    book = relationship("Book", back_populates="loans")


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
