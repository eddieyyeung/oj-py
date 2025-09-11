from unittest import TestCase

from leetcode.P1733.solution import Solution


class TestSolution(TestCase):
    def test(self):
        cases = [
            [2, [[1], [2], [1, 2]], [[1, 2], [1, 3], [2, 3]]]
        ]
        solution = Solution()
        for case in cases:
            print(solution.minimumTeachings(case[0], case[1], case[2]))
