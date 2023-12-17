from pathlib import Path
from tempfile import NamedTemporaryFile
import pytest
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session
from project import app, db

TEST_PATH = Path(__file__).parent.resolve()


@pytest.fixture
def db_session() -> Session:
    with NamedTemporaryFile(suffix=".sqlite", dir=TEST_PATH) as db_file, app.app_context():
        app.config.update({"SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_file}"})
        db.create_all()
        yield db.session
        db.drop_all()



