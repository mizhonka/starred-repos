import requests
from fastapi.testclient import TestClient
from dotenv import dotenv_values
from ..main import app

client=TestClient(app)

config = dotenv_values()
CLIENT_ID=config.get('CLIENT_ID')

def test_index_renders_login_when_not_logged_in():
    response=client.get('/')
    assert response.status_code==200
    assert 'Please login through Github to continue' in response.text

def test_logout_redirects_to_login_page():
    response=client.get('/logout')
    assert response.status_code==200
    assert 'Please login through Github to continue' in response.text

def test_return_json_when_not_logged_in_returns_empty():
    response=client.get('/return_json')
    assert response.status_code==200
    assert response.json()==[]

def test_get_user_data_error_without_access_token():
    response=client.get('/get_user_data')
    assert response.status_code==401
    assert response.json()=={'detail': 'Unauthorized: You need to be logged in'}

def test_get_access_token_error_when_code_is_invalid():
    response=client.get('/get_access_token?code=123')
    assert response.status_code==401
    assert response.json()=={'detail': 'Error: Bad verification code'}

def test_index_error_when_code_is_invalid():
    response=client.get('/?code=123')
    assert response.status_code==401
    assert response.json()=={'detail': 'Error: Bad verification code'}

def test_oauth_login_with_valid_client_id():
    response=requests.get('https://github.com/login/oauth/authorize?client_id='+CLIENT_ID)
    assert response.status_code==200
    assert 'oauth_app' in response.text

def test_regular_login_with_invalid_client_id():
    base_url='https://github.com/login/oauth/authorize?client_id=123'
    response=requests.get(base_url)
    assert response.status_code==200
    assert not 'oauth_app' in response.text


