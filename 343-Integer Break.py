# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-10 下午8:06
# @Email : wwymsn@163.com
# @Software: PyCharm

class Solution:
	def integerBreak(self, n):
		memo = [0]*(n+1)
		memo[1] = 1
		for i in range(2, n+1):
			for j in range(1, i):
				memo[i] = max(memo[i], j*(i-j), j*memo[i-j])
		return memo[n]


if __name__ == "__main__":
	test = Solution()
	print(test.integerBreak(10))
