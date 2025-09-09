import math
import sys
from functools import cache
from typing import TextIO


class Args:
    n: int
    c1: int
    c2: int
    persons: str


class Solution:

    # (c1+c2)*m - 2*c2*n + c2*(x1*x1 + x2*x2)
    @staticmethod
    def solve(args: Args):
        cnt_adults = args.persons.count('1')

        @cache
        def cal_price(m: int):
            p1 = (args.c1 + args.c2) * m
            p2 = -2 * args.c2 * args.n
            p3 = args.c2 * ((args.n // m + 1) * (args.n // m + 1) * (args.n % m) + (args.n // m) * (args.n // m) * (m - args.n % m))
            rst = p1 + p2 + p3

            # print("m: {}, rst: {}".format(m, rst))
            return rst

        rst = math.inf

        for i in range(1, cnt_adults + 1):
            rst = min(rst, cal_price(i))
        print(rst)

    @staticmethod
    def run(input: TextIO, output: TextIO):
        sys.stdin = input
        sys.stdout = output
        args = Args()
        line = list(map(int, input.readline().split()))
        args.n, args.c1, args.c2 = line[0], line[1], line[2]
        args.persons = input.readline()
        Solution.solve(args)


if __name__ == "__main__":
    Solution.run(sys.stdin, sys.stdout)
