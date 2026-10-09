from app import app

def test_app():
    assert app() == "CI/CD Demo"
