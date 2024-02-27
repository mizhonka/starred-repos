"""main program"""
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from dotenv import dotenv_values

app = FastAPI()
config = dotenv_values()

login_url = 'https://github.com/login/oauth/authorize?client_id=' + \
    config.get('CLIENT_ID')

templates = Jinja2Templates(directory="src/templates")


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    """renders homepage"""
    code=""
    print(code)
    if 'code' in request.query_params:
        code=request.query_params['code']
        return templates.TemplateResponse(name='logged.html', request=request)
    return templates.TemplateResponse(name='index.html', request=request)


@app.get('/login')
def login():
    """redirects to login screen"""
    return RedirectResponse(login_url)
