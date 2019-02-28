# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-28 下午10:16
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
因为给定的二叉搜索树中只有两个元素是交换了的，那么找到这两个位置，直接交换，就恢复了．
'''


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def __init__(self):
		self.pre = None
		self.first = None
		self.second = None

	def recoverTree(self, root: TreeNode) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""
		self.traverse(root)
		self.first.val, self.second.val = self.second.val, self.first.val

	def traverse(self, root):
		if not root:
			return
		self.traverse(root.left)
		if self.pre:
			if not self.first and (self.pre.val > root.val):
				self.first = self.pre
			if self.first and (self.pre.val > root.val):
				self.second = root
		self.pre = root

		self.traverse(root.right)