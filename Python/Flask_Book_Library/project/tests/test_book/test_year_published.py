import pytest
import sqlalchemy.exc
from project.books.models import Book
from .conftest import INVALID_VALUES, INJECTIONS, EXTREMES


@pytest.mark.parametrize("value", (
    2011,
    1996,
    1823
))
def test_valid_values(db_session, book, value):
    book.year_published = value
    db_session.add(book)
    db_session.commit()


@pytest.mark.parametrize("value", (
    100000000000,
    -1,
    0,
    "arbitrary string"
))
def test_invalid_values(db_session, book, value):
    book.year_published = value
    db_session.add(book)
    with pytest.raises(sqlalchemy.exc.SQLAlchemyError):
        db_session.commit()


@pytest.mark.parametrize("value", INJECTIONS)
def test_injections(db_session, book, value):
    book.year_published = value
    book.id = 1000
    db_session.add(book)
    db_session.commit()
    queried_book = db_session.query(Book).filter_by(id=1000).one()
    assert queried_book.year_published != value


@pytest.mark.parametrize("value", EXTREMES)
def test_extremes(db_session, book, value):
    book.year_published = value
    db_session.add(book)
    with pytest.raises(sqlalchemy.exc.SQLAlchemyError):
        db_session.commit()