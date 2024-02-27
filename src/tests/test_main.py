from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app
client=TestClient(app)

def test_render_index_when_not_logged_in():
    response=client.get('/')
    assert response.status_code==200
    assert "Login to GitHub" in response.text

def test_render_logged_when_logged_in():
    response=client.get('/?code=1234')
    assert response.status_code==200
    assert "Welcome" in response.text
