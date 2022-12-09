import unittest
from two_sum import two_sum_brute
from two_sum import two_sum_hash


class TestTwoSum(unittest.TestCase):
    def test_two_sum_brute1(self):
        nums = [2, 7, 11, 15]
        target = 9
        solution = [0, 1]
        result = two_sum_brute(nums, target)
        self.assertEqual(result, solution)

    def test_two_sum_brute2(self):
        nums = [3, 2, 4]
        target = 6
        solution = [1, 2]
        result = two_sum_brute(nums, target)
        self.assertEqual(result, solution)
        
    def test_two_sum_brute3(self):
        nums = [3, 3]
        target = 6
        solution = [0, 1]
        result = two_sum_brute(nums, target)
        self.assertEqual(result, solution)

    def test_two_sum_hash1(self):
        nums = [2, 7, 11, 15]
        target = 9
        solution = [0, 1]
        result = two_sum_hash(nums, target)
        self.assertEqual(result, solution)

    def test_two_sum_hash2(self):
        nums = [3, 2, 4]
        target = 6
        solution = [1, 2]
        result = two_sum_hash(nums, target)
        self.assertEqual(result, solution)

    def test_two_sum_hash3(self):
        nums = [3, 3]
        target = 6
        solution = [0, 1]
        result = two_sum_hash(nums, target)
        self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()
