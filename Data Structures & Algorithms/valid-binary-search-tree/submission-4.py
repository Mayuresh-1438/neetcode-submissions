# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        li = []
        def inorder(root):
            if not root:
                return 0
            inorder(root.left)
            li.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(1,len(li)):
            if li[i-1] >= li[i]:
                return False
        return True
            