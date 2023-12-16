import pytest

from project.books.models import Book


class BookDefaults:
    NAME = "The Four Agreements: A Practical Guide to Personal Freedom"
    AUTHOR = "Don Miguel Ruiz"
    YEAR_PUBLISHED = 1997
    BOOK_TYPE = "Social Sciences"
    STATUS = "available"

INVALID_VALUES = (42732173897982797,
    "1234567",
    "😇🎒🚧",)

INJECTIONS = (
    "' OR '1'='1",
    "'; DROP TABLE users; --",
    "<script>alert('XSS')</script>",
    "admin' --",
    "') OR ('1'='1",
    "javascript:alert('XSS')",
    "' OR 1=1--",
    "\"><script>alert('XSS')</script>",
    "' UNION SELECT NULL, username, password FROM users -- ",
    "\"><img src=x onerror=alert('XSS')>"
)

EXTREMES = (
    10*20,
    "longstring"*20
)

@pytest.fixture
def book():
    return Book(
        name=BookDefaults.NAME,
        author=BookDefaults.AUTHOR,
        year_published=BookDefaults.YEAR_PUBLISHED,
        book_type=BookDefaults.BOOK_TYPE,
        status=BookDefaults.STATUS
                )
