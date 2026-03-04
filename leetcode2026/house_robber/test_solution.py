from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rob(self):
        test_cases = [
            ([1, 2, 3, 1], 4),
            ([2, 7, 9, 3, 1], 12),
            ([5], 5),
            ([2, 1], 2),
            ([3, 3, 3, 3], 6),
            ([1, 2, 3, 4, 5], 9),
            ([0, 0, 0], 0),
            ([], 0),
        ]
        for nums, expected in test_cases:
            self.assertEqual(self.solution.rob(nums), expected)
