from unittest import TestCase

from leetcode2026.binary_tree_paths.solution import Solution, TreeNode


def build_tree(vals: list) -> TreeNode | None:
    """Build a binary tree from a level-order list (None means missing node)."""
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_leetcode_example1(self):
        # [1,2,3,null,5] -> ["1->2->5", "1->3"]
        root = build_tree([1, 2, 3, None, 5])
        self.assertCountEqual(self.solution.binaryTreePaths(root), ["1->2->5", "1->3"])

    def test_single_node(self):
        # Single node: root is also a leaf
        root = build_tree([1])
        self.assertCountEqual(self.solution.binaryTreePaths(root), ["1"])

    def test_empty_tree(self):
        self.assertCountEqual(self.solution.binaryTreePaths(None), [])

    def test_left_only_chain(self):
        # 1->2->3 (left only)
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertCountEqual(self.solution.binaryTreePaths(root), ["1->2->3"])

    def test_right_only_chain(self):
        # 1->2->3 (right only)
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertCountEqual(self.solution.binaryTreePaths(root), ["1->2->3"])

    def test_full_balanced_tree(self):
        # [1,2,3,4,5,6,7] -> 4 leaf paths
        root = build_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertCountEqual(
            self.solution.binaryTreePaths(root),
            ["1->2->4", "1->2->5", "1->3->6", "1->3->7"],
        )

    def test_left_heavy_two_levels(self):
        # [1,2,null,3] -> ["1->2->3"]
        root = build_tree([1, 2, None, 3])
        self.assertCountEqual(self.solution.binaryTreePaths(root), ["1->2->3"])

    def test_negative_values(self):
        root = build_tree([-1, -2, -3])
        self.assertCountEqual(self.solution.binaryTreePaths(root), ["-1->-2", "-1->-3"])

    def test_all_same_values(self):
        root = build_tree([5, 5, 5])
        self.assertCountEqual(self.solution.binaryTreePaths(root), ["5->5", "5->5"])
