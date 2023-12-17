import pytest
from .conftest import INVALID_VALUES, INJECTIONS, EXTREMES, create_book


@pytest.mark.parametrize("value", (
    "available",
    "unavailable",
    "available soon",
    "booked",
    "permanently unavailable"
))
def test_valid_values(db_session,  value):
    book = create_book(status=value)
    db_session.add(book)
    db_session.commit()


@pytest.mark.parametrize("value", (*INVALID_VALUES, *INJECTIONS, *EXTREMES))
def test_invalid_values(db_session,  value):
    with pytest.raises(Exception):
        book = create_book(status=value)
        db_session.add(book)
        db_session.commit()
