from codeforces.P774A.solution import Solution

if __name__ == '__main__':
    input = open("input.txt", "r+")
    output = open("output.txt", "w")
    for _ in range(4):
        Solution.run(input, output)