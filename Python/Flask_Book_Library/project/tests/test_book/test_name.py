import pytest
from .conftest import INVALID_VALUES, INJECTIONS, EXTREMES, create_book


@pytest.mark.parametrize("value", (
    "Journey Through the Stars",
    "The Culinary Art of Venice",
    "Whispers of the Ancient World",
    "Code and Creativity: The Digital Frontier",
    "Mysteries of the Rainforest"
))
def test_valid_values(db_session,  value):
    book = create_book(name=value)
    db_session.add(book)
    db_session.commit()


@pytest.mark.parametrize("value", (*INVALID_VALUES, *INJECTIONS, *EXTREMES))
def test_invalid_values(db_session,  value):
    with pytest.raises(Exception):
        book = create_book(name=value)
        db_session.add(book)
        db_session.commit()
