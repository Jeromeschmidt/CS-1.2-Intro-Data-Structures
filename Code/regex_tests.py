
import unittest
import re
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class RegexTest(unittest.TestCase):

    def test_removes_characters(self):
        string = "fds!@$##^@"
        init_len = len(string)
        string = re.sub("[^a-zA-Z]", '', string)
        assert init_len > len(string)

    def test_leaves_letters(self):
        string = "fds!@$##^@A"
        string = re.sub("[^a-zA-Z]", '', string)
        assert string == "fdsA"


if __name__ == '__main__':
    unittest.main()
