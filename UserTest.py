import unittest
from User import make_user

class UserTests(unittest.TestCase):
    def test_make_user(self):
        expected = { "name": "Jon Snow"}
        actual = make_user({"name": "Jon Snow"})
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
