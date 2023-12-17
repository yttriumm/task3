from .conftest import BookDefaults, create_book


def test_fields_assigned_correctly():
    book = create_book()
    assert book.book_type == BookDefaults.BOOK_TYPE
    assert book.name == BookDefaults.NAME
    assert book.author == BookDefaults.AUTHOR
    assert book.year_published == BookDefaults.YEAR_PUBLISHED
    assert book.status == BookDefaults.STATUS


def test_default_values_are_added_to_db(db_session):
    book = create_book()
    db_session.add(book)
    db_session.commit()


