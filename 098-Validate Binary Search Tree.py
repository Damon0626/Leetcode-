# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-25 下午10:39
# @Email : wwymsn@163.com
# @Software: PyCharm


'''
检验一棵树，是否是二叉搜索树
条件：
左子树上所有结点的值均小于它的根节点的值
右子树上所有结点的值均大于它的根结点的值
左、右子树也分别为二叉排序树
'''


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def isValidBST(self, root: TreeNode, left=float("-inf"), right=float("inf")) -> bool:

		if not root:
			return True
		if root.val <= left or root.val >= right:
			return False
		return self.isValidBST(root.left, left, min(root.val, right)) and self.isValidBST(root.right,  max(root.val, left), right)
