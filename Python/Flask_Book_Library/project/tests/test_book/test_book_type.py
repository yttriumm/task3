import pytest
from .conftest import INVALID_VALUES, INJECTIONS, EXTREMES, create_book


@pytest.mark.parametrize("value", ( "J.K. Rowling",
    "Fiction",
    "Non-Fiction",
    "Biography",
    "Science Fiction and Social Sciences"))
def test_valid_values(db_session,  value):
    book = create_book(book_type=value)
    db_session.add(book)
    db_session.commit()


@pytest.mark.parametrize("value", (*INVALID_VALUES, *INJECTIONS, *EXTREMES))
def test_invalid_values(db_session,  value):
    with pytest.raises(Exception):
        book = create_book(book_type=value)
        db_session.add(book)
        db_session.commit()
