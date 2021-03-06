package algorithem

func inorderTraversal(root *TreeNode) []int {
	var res []int
	var stack []*TreeNode
	for len(stack) != 0 || root != nil {
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]
		res = append(res, root.Val)
		stack = stack[0 : len(stack)-1]
		root = root.Right
	}
	return res
}
