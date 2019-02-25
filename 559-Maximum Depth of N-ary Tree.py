# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-25 下午10:35
# @Email : wwymsn@163.com
# @Software: PyCharm


"""
# Definition for a Node.
class Node:
	def __init__(self, val, children):
		self.val = val
		self.children = children
"""
'''
N叉树的最大深度，也是递归进行遍历，当然也可以诸层阅读，然后每读完一层，counter += 1
'''

class Solution:
	def maxDepth(self, root: 'Node') -> int:
		if not root:
			return 0
		if not root.children:
			return 1
		return max([self.maxDepth(i)+1 for i in root.children])
