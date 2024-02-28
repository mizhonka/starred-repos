"""module containing 'AccessToken' class"""

class AccessToken:
    """class for storing the access token"""

    def __init__(self):
        """class constructor"""
        self._token=""

    def set(self, token):
        """assign the access token"""
        self._token=token

    def get(self):
        """return the access token"""
        return self._token

    def remove(self):
        """set the access token to an empty string"""
        self._token=""
