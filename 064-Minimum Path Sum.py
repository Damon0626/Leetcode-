# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-10 下午7:27
# @Email : wwymsn@163.com
# @Software: PyCharm

class Solution:
	def minPathSum(self, grid) -> int:

		m = len(grid)
		n = len(grid[0])

		for i in range(1, n):
			grid[0][i] += grid[0][i-1]
		for i in range(1, m):
			grid[i][0] += grid[i-1][0]

		for i in range(1, m):
			for j in range(1, n):
				grid[i][j] += min(grid[i-1][j], grid[i][j-1])

		return grid[-1][-1]


if __name__ == "__main__":
	text = Solution()
	grid = [[1,4,8,6,2,2,1,7],\
	        [4,7,3,1,4,5,5,1],\
	        [8,8,2,1,1,8,0,1],\
	        [8,9,2,9,8,0,8,9],\
	        [5,7,5,7,1,8,5,5],\
	        [7,0,9,4,5,6,5,6],\
	        [4,9,9,7,9,1,9,0]]
	print(text.minPathSum(grid))