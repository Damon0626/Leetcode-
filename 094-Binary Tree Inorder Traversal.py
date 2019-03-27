# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-27 下午10:28
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
	\
	 2
	/
   3

Output: [1,3,2]
'''

# 可以使用递归的方法, 也可以使用循环的方法
# Definition for a binary tree node.


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def __init__(self):
		self.res = []
	def inorderTraversal(self, root: TreeNode) -> List[int]:
		'''使用递归的方法'''
		# 终止条件
		if not root:
			return []
		else:
			# drill down
			self.inorderTraversal(root.left)
			self.res.append(root.val)
			self.inorderTraversal(root.right)
		return self.res
