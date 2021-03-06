# 1. 使用一个栈保存结点（列表实现）；
# 2. 如果结点存在，入栈，然后将当前指针指向左子树，直到为空；
# 3. 当前结点不存在，则出栈栈顶元素，并把当前指针指向栈顶元素的右子树；
# 4. 栈不为空，循环2、3步。
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        cur = root
        res = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res