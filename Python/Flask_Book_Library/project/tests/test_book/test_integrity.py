from project.books.models import Book
from .conftest import BookDefaults


def test_fields_assigned_correctly(book):
    assert book.book_type == BookDefaults.BOOK_TYPE
    assert book.name == BookDefaults.NAME
    assert book.author == BookDefaults.AUTHOR
    assert book.year_published == BookDefaults.YEAR_PUBLISHED
    assert book.status == BookDefaults.STATUS


def test_default_values_pass(db_session, book):
    db_session.add(book)
    db_session.commit()

