import unittest
from long_sub_no_repeat import long_sub_no_repeat


class TestLongSubNoRepeat(unittest.TestCase):
    def test_long_sub_no_repeat1(self):
        s = "abcabcbb"
        solution = 3
        result = long_sub_no_repeat(s)
        self.assertEqual(result, solution)

    def test_long_sub_no_repeat2(self):
        s = "pwwkew"
        solution = 3
        result = long_sub_no_repeat(s)
        self.assertEqual(result, solution)

    def test_long_sub_no_repeat3(self):
        s = "bbbbb"
        solution = 1
        result = long_sub_no_repeat(s)
        self.assertEqual(result, solution)

    def test_long_sub_no_repeat4(self):
        s = " "
        solution = 1
        result = long_sub_no_repeat(s)
        self.assertEqual(result, solution)

    def test_long_sub_no_repeat5(self):
        s = "ma"
        solution = 2
        result = long_sub_no_repeat(s)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
