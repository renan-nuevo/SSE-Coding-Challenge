import unittest
from helpers import is_palindrome
from main import longest_palindrome

class TestSum(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('madam'))
        self.assertTrue(is_palindrome('a'))
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('lkhdddsssdddhkl'))
        self.assertFalse(is_palindrome('asdfs'))
        self.assertFalse(is_palindrome('aaa'))
        self.assertFalse(is_palindrome('tinitit'))
        self.assertFalse(is_palindrome('notpalindrome'))

    def test_is_palindrome(self):
        self.assertEqual(longest_palindrome('madam'), 'madam', 'Correct answer should be madam')
        self.assertEqual(longest_palindrome('sdfsaaabbbaaaaskdfla'), 'aaabbbaaa', 'Correct answer should be aaabbbaaa')
        self.assertEqual(longest_palindrome('initinit'), 'initini', 'Correct answer should be initini')
        self.assertEqual(longest_palindrome('madaminitini'), 'initini', 'Correct answer should be initini')
        self.assertEqual(longest_palindrome('aabasaaasadb'), 'asaaasa', 'Correct answer should be asaaasa')



if __name__ == '__main__':
    unittest.main()
