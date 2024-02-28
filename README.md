![CI badge](https://github.com/mizhonka/starred-repos/actions/workflows/main.yml/badge.svg)

# Starred Repos

With this web-app, you can view your starred repositories on GitHub, and export them in a JSON format.

## Installation (Linux & Windows)

1. Clone this repository and navigate to the root directory
2. Create _.env_ file with the following contents:
   ```
   CLIENT_ID=<your OAuth app Client ID>
   CLIENT_SECRET=<client secret>
   ```
3. Create a virtual environment with
   ```
   python3 -m venv venv 
   ```
4. Enter virtual environment with
   
   Linux:
   ```
   source venv/bin/activate
   ```
   Windows:
   ```
   venv\Scripts\activate
   ```
5. Install dependencies with
   ```
   pip install -r requirements.txt 
   ```
6. Run application with
   ```
   uvicorn src.main:app
   ```
