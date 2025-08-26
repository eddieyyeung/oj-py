from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal_length_square = 0
        max_square = 0
        for dimension in dimensions:
            length, width = dimension[0], dimension[1]
            diagonal_length_square = length * length + width * width
            square = length * width
            if diagonal_length_square > max_diagonal_length_square:
                max_diagonal_length_square = diagonal_length_square
                max_square = square
            elif diagonal_length_square == max_diagonal_length_square:
                if square > max_square:
                    max_square = square
        return max_square
