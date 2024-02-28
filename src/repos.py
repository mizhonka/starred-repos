"""module containing 'Repos' class"""

class Repos:
    """class for storing starred repositories"""

    def __init__(self):
        """class constructor"""
        self._json_repos=[]

    def add(self, starred):
        """adds new json object to the list"""
        self._json_repos.append(starred)

    def get(self):
        """returns the list of json objects"""
        return self._json_repos

    def empty(self):
        """clears the list of json objects"""
        self._json_repos=[]
