from typing import List

MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [''] * n
        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return
            for ch in MAPPING[int(digits[i])]:
                path[i] = ch
                dfs(i+1)
                path[i] = ''
        dfs(0)
        return ans
