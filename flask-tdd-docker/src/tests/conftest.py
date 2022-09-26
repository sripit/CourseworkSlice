#unittest coding: smallest piece of code that can be logically isolated in a system
import pytest

from src import create_app, db
from src.api.users.models import User

#fixtures: reusable objects for tests
    #have a scope associated with them, which indicates how
    #fixture is invoked
    #essentially initializes a system

    #scope details for fixtures:
        #1. for a function, the fixture is invoked once per test function
        #2. for a class, the fixture is invoked once per test class
        #3. for a module, invoked once per test module
        #4. session -once per test session
@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.from_object('src.config.TestingConfig')
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()

# to add a few users, add a fixture that uses 'factory as fixture'
#pattern
    #instead of running data correctly, fixture returns a function that gene
    #rates data.
    #useful when the result of a fixture is needed multiple times
@pytest.fixture(scope='function')
def add_user():
    def _add_user(username, email):
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user
    return _add_user

