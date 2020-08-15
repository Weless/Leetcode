package main

func searchBST(root *TreeNode, val int) *TreeNode {
	if root == nil || root.Val == val{
		return root
	}
	if val < root.Val{
		return searchBST(root.Left,val)
	}else{
		return searchBST(root.Right,val)
	}
}