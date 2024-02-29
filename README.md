![CI badge](https://github.com/mizhonka/starred-repos/actions/workflows/main.yml/badge.svg)

# Starred Repos

With this web-app, you can view a summary of your starred repositories on GitHub, and export them in a JSON format.

## Installation (Linux & Windows)

1. [Create an OAuth app](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app). Homepage / callback URL is the local address where the uvicorn server will run  
   (http:<span></span>//127.0.0.1:8000 by default)
2. Clone this repository and navigate to the root directory
3. Create _.env_ file with the following contents:
   ```
   CLIENT_ID=<your OAuth app Client ID>
   CLIENT_SECRET=<client secret>
   ```
4. Create a virtual environment with
   ```
   python3 -m venv venv 
   ```
5. Enter virtual environment with
   
   Linux:
   ```
   source venv/bin/activate
   ```
   Windows:
   ```
   venv\Scripts\activate
   ```
6. Install dependencies with
   ```
   pip install -r requirements.txt 
   ```
7. Run application with
   ```
   uvicorn src.main:app
   ```

## Testing

To run tests and generate a coverage report, run
```
coverage run -m pytest src/tests/
```
inside the virtual environment.  

To print out a coverage report, run
```
coverage report
```
or for a HTML-format
```
coverage html
```

See pylint-scoring with
```
pylint src
```
