# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-25 下午10:29
# @Email : wwymsn@163.com
# @Software: PyCharm

# Definition for a binary tree node.

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

'''
寻找二叉搜索树某两个元素的最小公共祖先：
使用递归
'''


class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		if root.val > p.val and root.val > q.val:
			return self.lowestCommonAncestor(root.left, p, q)
		if root.val < p.val and root.val < q.val:
			return self.lowestCommonAncestor(root.right, p, q)
		return root
