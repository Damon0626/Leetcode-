# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-5 下午9:47
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
主要使用了BFS(广度优先遍历),借鉴大神的代码
'''


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		ans, level = [], [root]
		while root and level:
			ans.append([node.val for node in level])
			subT = [(node.left, node.right) for node in level]  # 遍历每一层上所有的node
			level = [node for pair in subT for node in pair if node]  # 注意上边的元组(node.left, node.right)
		return ans

