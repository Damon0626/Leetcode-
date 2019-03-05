# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-5 下午9:50
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
深度优先遍历DFS
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:
		if not word:
			return True

		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == word[0]:
					if self.dfs_search(board, i, j, word):
						return True
		return False

	def dfs_search(self, board, i, j, word):
		if not word:
			return True
		if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0]:
			return False
		backup = board[i][j]
		board[i][j] = '#'  # 将已经计算过的点赋值为‘#’防止被重复使用

		result = self.dfs_search(board, i, j - 1, word[1:]) or \
				 self.dfs_search(board, i, j + 1, word[1:]) or \
				 self.dfs_search(board, i - 1, j, word[1:]) or \
				 self.dfs_search(board, i + 1, j, word[1:])  # 只要有一个方向寻找到了，利用dfs就可以逐层寻到底。

		board[i][j] = backup  # 恢复被赋值的坐标点位置。
		return result
