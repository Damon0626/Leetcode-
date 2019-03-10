# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-10 下午8:57
# @Email : wwymsn@163.com
# @Software: PyCharm


class Solution:
	def numSquares(self, n):
		# 最优子结构
		# 完美平方数 = min(dp[i]+dp[n-i], dp[n]) i = 1~n//2, 因为有的数字除了分解，也可以是自身

		# 状态转移方程
		# dp[i] = min(dp[j]+dp[i-j], dp[i])

		dp = [float('inf')]*(n+1)
		dp[1] = 1

		for i in range(1, n+1):
			if int(i**0.5)**2 == i:
				dp[i] = 1
			else:
				for j in range(1, i//2+1):
					dp[i] = min(dp[j]+dp[i-j], dp[i])

		print(dp)


if __name__ == "__main__":
	test = Solution()
	test.numSquares(5156)
