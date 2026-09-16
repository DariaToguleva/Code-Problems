# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        maxi = 0
        return self.dep(root, maxi)

    def dep(self, node, maxi):
        if not node:
            return maxi
        return max(self.dep(node.left, maxi + 1), self.dep(node.right, maxi + 1))    