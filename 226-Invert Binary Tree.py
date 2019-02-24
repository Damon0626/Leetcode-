# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-24 下午7:19
# @Email : wwymsn@163.com
# @Software: PyCharm

# 反转二叉树
# Definition for a binary tree node.
# class TreeNode:
# 	 def __init__(self, x):
# 		 self.val = x
# 		 self.left = None
# 		 self.right = None


class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode:
		if root:
			root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)  # 递归算法
			print(root.val)
		return root
