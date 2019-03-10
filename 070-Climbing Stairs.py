# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-10 下午4:26
# @Email : wwymsn@163.com
# @Software: PyCharm


class Solution:
	def climbStairs(self, n: int) -> int:
		if n == 0:
			return 0
		if n == 1:
			return 1
		if n == 2:
			return 2

		x, y = 1, 1
		for i in range(2, n + 1):
			x, y = y, x + y
		return y


if __name__ == "__main__":
	test = Solution()
	print(test.climbStairs(10))
