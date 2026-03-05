from unittest import TestCase

from leetcode2026.letter_combinations_of_a_phone_number.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example(self):
        self.assertCountEqual(
            self.solution.letterCombinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )

    def test_empty(self):
        self.assertCountEqual(self.solution.letterCombinations(""), [])

    def test_single_digit_three_letters(self):
        self.assertCountEqual(self.solution.letterCombinations("2"), ["a", "b", "c"])

    def test_single_digit_four_letters(self):
        self.assertCountEqual(
            self.solution.letterCombinations("9"), ["w", "x", "y", "z"]
        )

    def test_two_four_letter_keys(self):
        self.assertCountEqual(
            self.solution.letterCombinations("79"),
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
        )

    def test_three_digits(self):
        self.assertCountEqual(
            self.solution.letterCombinations("234"),
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
        )

    def test_repeated_digit(self):
        self.assertCountEqual(
            self.solution.letterCombinations("22"),
            ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"],
        )
