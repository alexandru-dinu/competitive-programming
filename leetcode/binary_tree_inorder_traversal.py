# https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        acc = []
        acc.extend(self.inorderTraversal(root.left))
        acc.append(root.val)
        acc.extend(self.inorderTraversal(root.right))

        return acc
