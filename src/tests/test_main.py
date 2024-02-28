from fastapi import FastAPI
from fastapi.testclient import TestClient
from dotenv import dotenv_values

config = dotenv_values()
CLIENT_ID=config.get('CLIENT_ID')
CLIENT_SECRET=config.get('CLIENT_SECRET')

from ..main import app
client=TestClient(app)

def test_render_index_when_not_logged_in():
    response=client.get('/')
    assert response.status_code==200
    assert "Please login" in response.text

def test_render_logged_when_logged_in():
    base_url='https://github.com/login/oauth/authorize'
    login_url = base_url+'?client_id='+CLIENT_ID
    response=client.get(login_url)
    assert response.status_code==200
