import unittest
from main import Solution
from main import ListNode


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution
        self.given = [ListNode(1, ListNode(
            2, ListNode(3, ListNode(4, ListNode(5))))), 2]

    def test_given(self):
        pass


if __name__ == '__main__':
    unittest.main()
