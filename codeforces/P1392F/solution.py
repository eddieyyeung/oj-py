import sys
from typing import TextIO


class Args:
    n: int
    sum: int = 0


class Solution:

    @staticmethod
    def solve(args: Args):
        a = (args.sum - args.n * (args.n - 1) // 2) // args.n
        b = int((args.sum - args.n * (args.n - 1) // 2) % args.n)

        for i in range(0, args.n):
            r = i + a
            if i + 1 <= b:
                r += 1
            print("{}".format(int(r)), end=" ")

        print()

    @staticmethod
    def run(input: TextIO, output: TextIO):
        sys.stdin = input
        sys.stdout = output
        args = Args()
        args.n = int(input.readline())
        nums = list(map(int, input.readline().split()))
        args.sum = sum(nums)
        Solution.solve(args)


if __name__ == "__main__":
    Solution.run(sys.stdin, sys.stdout)
