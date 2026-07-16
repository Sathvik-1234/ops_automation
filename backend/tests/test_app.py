import pytest
from app import app

def test_homepage():
    # Create a test client for your Flask app
    client = app.test_client()
    response = client.get('/')
    # Assert that the app returns a 200 OK status
    assert response.status_code == 200