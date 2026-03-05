from unittest import TestCase

from leetcode2026.house_robber.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_non_adjacent(self):
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)

    def test_longer_sequence(self):
        self.assertEqual(self.solution.rob([2, 7, 9, 3, 1]), 12)

    def test_single_element(self):
        self.assertEqual(self.solution.rob([5]), 5)

    def test_two_elements(self):
        self.assertEqual(self.solution.rob([2, 1]), 2)

    def test_all_same(self):
        self.assertEqual(self.solution.rob([3, 3, 3, 3]), 6)

    def test_increasing(self):
        self.assertEqual(self.solution.rob([1, 2, 3, 4, 5]), 9)

    def test_all_zeros(self):
        self.assertEqual(self.solution.rob([0, 0, 0]), 0)

    def test_empty(self):
        self.assertEqual(self.solution.rob([]), 0)
