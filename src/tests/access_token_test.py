import unittest
from ..access_token import AccessToken

class TestAccessToken(unittest.TestCase):
    def setUp(self):
        self.token=AccessToken()

    def test_set_token_matches(self):
        self.token.set('abc')
        self.assertEqual(self.token.get(), 'abc')

    def test_remove_clears_token(self):
        self.token.set('abc')
        self.token.remove()
        self.assertEqual(self.token.get(), '')

