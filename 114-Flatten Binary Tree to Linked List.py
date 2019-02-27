# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-27 下午10:29
# @Email : wwymsn@163.com
# @Software: PyCharm


# Definition for a binary tree node.
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None

# 本题目中，先是找到右子树的叶结点，诸层反向回来，得到最终的结果．１
class Solution:
	def __init__(self):
		self.pre = None

	def flatten(self, root: TreeNode) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""

		if not root:
			return
		self.flatten(root.right)
		self.flatten(root.left)

		root.right = self.pre
		root.left = None
		self.pre = root
