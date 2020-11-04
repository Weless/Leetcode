class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = 0
        self.count = 0
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.count += 1
            if self.count == k:
                self.res = root.val
                return
            dfs(root.right)
        dfs(root)
        return res