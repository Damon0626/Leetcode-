# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-27 下午10:27
# @Email : wwymsn@163.com
# @Software: PyCharm


# Definition for a binary tree node.
# class TreeNode:
# 	 def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None

# 注意当结点只有一个左叶节点或右结点，此时父结点的最小深度不是0，而是2
class Solution:
	def minDepth(self, root: TreeNode) -> int:
		if not root:
			return 0
		if not root.left or not root.right:
			return self.minDepth(root.left)+self.minDepth(root.right)+1  # 需要注意的地方
		return min(self.minDepth(root.left)+1, self.minDepth(root.right)+1)
