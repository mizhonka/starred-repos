import unittest
from ..repos import Repos

class TestRepos(unittest.TestCase):
    def setUp(self):
        self.stars=Repos()

    def test_set_content_matches(self):
        obj_a={'index': 0, 'name':'a'}
        obj_b={'index':1, 'name':'b'}
        self.stars.add(obj_a)
        self.stars.add(obj_b)
        self.assertEqual(self.stars.get(), [obj_a, obj_b])

    def test_empty_clears_list(self):
        self.stars.add({'item': 'this'})
        self.stars.empty()
        self.assertEqual(self.stars.get(), [])
