# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        path = []
        def dfs(node):
            if node is None:
                return

            path.append(str(node.val))
            if not node.left and not node.right:
                ans.append("->".join(path))
            dfs(node.left)
            dfs(node.right)
            path.pop()

        dfs(root)
        return ans