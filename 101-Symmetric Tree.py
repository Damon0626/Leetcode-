# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-28 下午10:14
# @Email : wwymsn@163.com
# @Software: PyCharm


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:
		if not root:
			return True
		return self.isMirror(root.left, root.right)

	def isMirror(self, left, right):
		if not left and not right:
			return True
		if not left or not right or left.val != right.val:
			return False
		# 最外层的，最内层的,原作者的思想真实敏捷
		return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

