# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-26 下午10:22
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
	def hasPathSum(self, root: TreeNode, sum: int) -> bool:
		# 运用递归的方法
		# 从根结点开始，用sum去减根节点的值，最终和叶节点的值进行比较，一致则存在，否则不存在

		# 终止条件
		if not root:
			return False
		if not root.left and not root.right and sum == root.val:
			return True

		# 当前层的操作
		sum -= root.val

		# drill down
		return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
