from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res,stack = [],[]
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.right
            if stack:
                t = stack.pop()
                root = t.left
        return res[::-1]