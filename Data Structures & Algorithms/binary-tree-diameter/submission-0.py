# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi=0

        def height(root):
            m=0
            if root:
                m+=1
                left=height(root.left)
                right=height(root.right)
                self.maxi=max(self.maxi, left+right)
                m+=max(left,right)
            return m

        height(root)
        return self.maxi