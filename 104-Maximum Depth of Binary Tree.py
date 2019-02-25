# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-25 下午10:37
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
二叉树最大深度，注意终止条件．
'''


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def maxDepth(self, root: TreeNode) -> int:
		if not root:
			return 0

		return max(self.maxDepth(root.left), self.maxDepth(root.right))+1