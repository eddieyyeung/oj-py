from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            rst = max(dfs(i-1), dfs(i-2) + nums[i])
            return rst

        return dfs(len(nums)-1)