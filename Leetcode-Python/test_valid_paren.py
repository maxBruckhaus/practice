import unittest
from valid_paren import valid_paren


class TestLongSubNoRepeat(unittest.TestCase):
    def test_valid_paren1(self):
        s = "()"
        solution = True
        result = valid_paren(s)
        self.assertEqual(solution, result)

    def test_valid_paren2(self):
        s = "(()"
        solution = False
        result = valid_paren(s)
        self.assertEqual(solution, result)

    def test_valid_paren3(self):
        s = ")(["
        solution = False
        result = valid_paren(s)
        self.assertEqual(solution, result)

    def test_valid_paren4(self):
        s = "([)]"
        solution = False
        result = valid_paren(s)
        self.assertEqual(solution, result)

    def test_valid_paren5(self):
        s = "{[]}"
        solution = True
        result = valid_paren(s)
        self.assertEqual(solution, result)


if __name__ == '__main__':
    unittest.main()
