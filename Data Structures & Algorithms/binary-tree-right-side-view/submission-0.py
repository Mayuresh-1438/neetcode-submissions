# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        stack = []
        stack.append(root.val)
        while q:
            val = stack.pop()
            res.append(val)
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    stack.append(node.left.val)
                if node.right:
                    q.append(node.right)   
                    stack.append(node.right.val)
        return res
