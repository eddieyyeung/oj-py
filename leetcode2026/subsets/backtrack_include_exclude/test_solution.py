from unittest import TestCase

from leetcode2026.subsets.backtrack_include_exclude.solution import Solution


def sorted_subsets(result: list[list[int]]) -> list[list[int]]:
    return sorted(sorted(s) for s in result)


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertEqual(
            sorted_subsets(self.solution.subsets([1, 2, 3])),
            sorted_subsets([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
        )

    def test_single_element(self):
        self.assertEqual(
            sorted_subsets(self.solution.subsets([1])),
            sorted_subsets([[], [1]]),
        )

    def test_empty(self):
        self.assertEqual(sorted_subsets(self.solution.subsets([])), [[]])

    def test_two_elements(self):
        self.assertEqual(
            sorted_subsets(self.solution.subsets([1, 2])),
            sorted_subsets([[], [1], [2], [1, 2]]),
        )

    def test_negative_values(self):
        self.assertEqual(
            sorted_subsets(self.solution.subsets([-1, 0, 1])),
            sorted_subsets([[], [-1], [0], [1], [-1, 0], [-1, 1], [0, 1], [-1, 0, 1]]),
        )
