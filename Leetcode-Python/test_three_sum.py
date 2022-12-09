import unittest
from three_sum import three_sum_cubic
from three_sum import three_sum_quadratic


class TestThreeSum(unittest.TestCase):
    def test_three_sum_cubic(self):
        nums1 = [-1, 0, 1, 2, -1, -4]
        result = three_sum_cubic(nums1)
        answer = [[-1, 0, 1], [-1, 2, -1]]
        self.assertEqual(result, answer)

    def test_three_sum_quadratic(self):
        nums1 = [-1, 0, 1, 2, -1, -4]
        result = three_sum_quadratic(nums1)
        result_list = list(result)
        answer = [(-1, 0, 1), (-1, -1, 2)]
        self.assertEqual(result_list, answer)


if __name__ == '__main__':
    unittest.main()
