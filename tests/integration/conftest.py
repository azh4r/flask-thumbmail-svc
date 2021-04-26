from app.main import create_app
import pytest

@pytest.fixture()
def client():
    app = create_app()
    app.config.from_object("app.config.TestingConfig")
    with app.app_context():
        yield app