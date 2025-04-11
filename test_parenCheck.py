import unittest
from parenCheck import is_balanced

class TestParenChecker(unittest.TestCase):

    def test_balanced_cases(self):
        self.assertTrue(is_balanced("()"))
        self.assertTrue(is_balanced("({[]})"))
        self.assertTrue(is_balanced("[{()}]"))
        self.assertTrue(is_balanced("(([]){})"))
    
    def test_unbalanced_cases(self):
        self.assertFalse(is_balanced("([)]"))
        self.assertFalse(is_balanced("((()"))
        self.assertFalse(is_balanced("{[}"))
        self.assertFalse(is_balanced("]"))
        self.assertFalse(is_balanced("("))
        self.assertFalse(is_balanced(")("))

    def test_empty_string(self):
        self.assertTrue(is_balanced(""))

if __name__ == '__main__':
    unittest.main()

