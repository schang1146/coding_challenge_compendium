import unittest
from main import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution
        self.given = [3, 10, 5, 25, 2, 8]

    def test_given(self):
        self.assertEqual(Solution.findMaximumXOR_hashset(self, self.given), 28)


if __name__ == '__main__':
    unittest.main()
