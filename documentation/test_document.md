# Testing Document

## Coverage Report

![coverage.png](https://github.com/mizhonka/starred-repos/blob/main/documentation/coverage.png)

## Tested Features

### AccessToken

* .get() returns a correct string after .set()
* .get() returns empty string after .remove()A

### Repos

* .get() returns a correct list of JSON-objects after .set()
* .get() returns an empty list after .empty()

### main.py

* Path '/' renders login page, when access_token and code -parameter are empty
* Path '/logout' redirects to login page
* Path '/return_json' returns an empty list, when not logged in
* Path '/get_user_data' returns a 401 error, when access_token -parameter is empty
* Path '/get_access_token' returns a 401 error, when code -parameter is not valid
* Path '/' redirects and returns a 401 error, when code -parameter is not valid
* Address 'https:/<span></span>/github.com/login/oauth/authorize?client_id=' redirects to OAuth login page, when client_id -parameter is valid
* Address 'https:/<span></span>/github.com/login/oauth/authorize?client_id=' redirects to regular login page, when client_id -parameter is not valid
