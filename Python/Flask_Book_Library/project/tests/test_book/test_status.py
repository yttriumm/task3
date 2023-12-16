import pytest
import sqlalchemy.exc
from project.books.models import Book
from .conftest import INVALID_VALUES, INJECTIONS, EXTREMES


@pytest.mark.parametrize("value", (
    "available",
    "unavailable",
    "available soon",
    "booked",
    "permanently unavailable"
))
def test_valid_values(db_session, book, value):
    book.status = value
    db_session.add(book)
    db_session.commit()


@pytest.mark.parametrize("value", INVALID_VALUES)
def test_invalid_values(db_session, book, value):
    book.status = value
    db_session.add(book)
    with pytest.raises(sqlalchemy.exc.SQLAlchemyError):
        db_session.commit()


@pytest.mark.parametrize("value", INJECTIONS)
def test_injections(db_session, book, value):
    book.status = value
    book.id = 1000
    db_session.add(book)
    db_session.commit()
    queried_book = db_session.query(Book).filter_by(id=1000).one()
    assert queried_book.status != value


@pytest.mark.parametrize("value", EXTREMES)
def test_extremes(db_session, book, value):
    book.status = value
    db_session.add(book)
    with pytest.raises(sqlalchemy.exc.SQLAlchemyError):
        db_session.commit()