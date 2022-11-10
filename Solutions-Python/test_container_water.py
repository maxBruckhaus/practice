import unittest
from container_water import max_area_cubic
from container_water import max_area_linear


class TestContainerWater(unittest.TestCase):
    def test_container_cubic(self):
        h1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        result = max_area_cubic(h1)
        self.assertEqual(result, 49)

    def test_container_linear(self):
        h1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        result = max_area_linear(h1)
        self.assertEqual(result, 49)


if __name__ == '__main__':
    unittest.main()