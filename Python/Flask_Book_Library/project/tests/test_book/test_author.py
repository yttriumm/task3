import pytest
from .conftest import INVALID_VALUES, INJECTIONS, EXTREMES, create_book


@pytest.mark.parametrize("value", ( "J.K. Rowling",
    "Gabriel García Márquez",
    "Chimamanda Ngozi Adichie",
    "Haruki Murakami",
    "Ngũgĩ wa Thiong'o"))
def test_valid_values(db_session,  value):
    book = create_book(author=value)
    db_session.add(book)
    db_session.commit()


@pytest.mark.parametrize("value", (*INVALID_VALUES, *INJECTIONS, *EXTREMES))
def test_invalid_values(db_session,  value):
    with pytest.raises(Exception):
        book = create_book(author=value)
        db_session.add(book)
        db_session.commit()