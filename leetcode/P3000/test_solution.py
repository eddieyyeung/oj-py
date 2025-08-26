from typing import List
from unittest import TestCase

from leetcode.P3000.solution import Solution


class TestSolution(TestCase):
    def test_area_of_max_diagonal(self):
        cases = [
            [[9, 3], [8, 6]],
            [[3, 4], [4, 3]]
        ]
        solution = Solution()
        for case in cases:
            print(solution.areaOfMaxDiagonal(case))
