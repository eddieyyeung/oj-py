from unittest import TestCase

from leetcode2026.letter_combinations_of_a_phone_number.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_letterCombinations(self):
        test_cases = [
            # 题目样例
            ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            # 空输入
            ("", []),
            # 单数字（3字母键）
            ("2", ["a", "b", "c"]),
            # 单数字（4字母键）
            ("9", ["w", "x", "y", "z"]),
            # 两个4字母键
            (
                "79",
                [
                    "pw",
                    "px",
                    "py",
                    "pz",
                    "qw",
                    "qx",
                    "qy",
                    "qz",
                    "rw",
                    "rx",
                    "ry",
                    "rz",
                    "sw",
                    "sx",
                    "sy",
                    "sz",
                ],
            ),
            # 三位数字（3*3*3=27种）
            (
                "234",
                [
                    "adg",
                    "adh",
                    "adi",
                    "aeg",
                    "aeh",
                    "aei",
                    "afg",
                    "afh",
                    "afi",
                    "bdg",
                    "bdh",
                    "bdi",
                    "beg",
                    "beh",
                    "bei",
                    "bfg",
                    "bfh",
                    "bfi",
                    "cdg",
                    "cdh",
                    "cdi",
                    "ceg",
                    "ceh",
                    "cei",
                    "cfg",
                    "cfh",
                    "cfi",
                ],
            ),
            # 相同数字重复
            ("22", ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]),
        ]
        for digits, expected in test_cases:
            self.assertCountEqual(self.solution.letterCombinations(digits), expected)
