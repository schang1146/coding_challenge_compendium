import unittest
from main import Solution


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_example1(self):
        self.assertEqual(Solution.divisorGame_dp(self, 2), True)

    def test_example2(self):
        self.assertEqual(Solution.divisorGame_dp(self, 3), False)


if __name__ == '__main__':
    unittest.main()
