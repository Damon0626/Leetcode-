# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-26 下午10:23
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
	def pathSum(self, root: TreeNode, sum_i: int) -> List[List[int]]:
		# DFS + stack
		#         if not root:
		#             return []
		#         res = []
		#         stack = [(root, [root.val])]

		#         while stack:
		#             curr, ls = stack.pop()
		#             if not curr.left and not curr.right and sum(ls) == sum_i:
		#                 res.append(ls)
		#             if curr.right:
		#                 stack.append((curr.right, ls+[curr.right.val]))
		#             if curr.left:
		#                 stack.append((curr.left, ls+[curr.left.val]))

		#         return res
		# BFS + queue
		if not root:
			return []
		res = []
		queue = [(root, [root.val])]
		while queue:
			curr, ls = queue.pop(0)
			if not curr.left and not curr.right and sum(ls) == sum_i:
				res.append(ls)
			if curr.left:
				queue.append((curr.left, ls + [curr.left.val]))
			if curr.right:
				queue.append((curr.right, ls + [curr.right.val]))
		return resd