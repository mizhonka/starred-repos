"""main program"""
import requests
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from dotenv import dotenv_values

app = FastAPI()

config = dotenv_values()
CLIENT_ID=config.get('CLIENT_ID')
CLIENT_SECRET=config.get('CLIENT_SECRET')

templates = Jinja2Templates(directory="src/templates")
templates.env.autoescape=False

@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    """renders homepage"""
    code=""
    if 'code' in request.query_params:
        code=request.query_params['code']
        return RedirectResponse('/get_access_token?code='+code)
    return templates.TemplateResponse(name='index.html', request=request)

@app.get('/get_user_data')
def get_user_data(request: Request):
    """gets user data from github api and renders html page to display it"""
    base_url='https://api.github.com/user'
    token=request.query_params['access_token']
    response=requests.get(base_url, headers={'Authorization':'Bearer ' + token}, timeout=5)
    result=response.json()['login']
    return templates.TemplateResponse('logged.html', {'request': request, 'name':result})

@app.get('/get_access_token')
def get_access_token(request: Request):
    """gets oauth access token and redirects to fetch user data"""
    base_url='https://github.com/login/oauth/access_token'
    code=request.query_params['code']
    access_url=base_url+'?client_id='+CLIENT_ID+'&client_secret='+CLIENT_SECRET+'&code='+code
    response=requests.get(access_url, headers={'Accept': 'application/json'}, timeout=5)
    token=response.json()['access_token']
    return RedirectResponse('/get_user_data?access_token='+token)

@app.get('/login')
def login():
    """redirects to login screen"""
    base_url='https://github.com/login/oauth/authorize'
    login_url = base_url+'?client_id='+CLIENT_ID
    return RedirectResponse(login_url)
