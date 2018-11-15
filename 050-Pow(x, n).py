# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-4 下午10:24
# @Email : wwymsn@163.com
# @Software: PyCharm


class Solution:
	def myPow(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		# method1:
		'''
		return x**n
		'''
		# method2:递归
		if n == 0:
			return 1
		if n < 0:
			return 1/self.myPow(x, -n)
		if n % 2:
			return x * self.myPow(x, n-1)
		return self.myPow(x*x, int(n/2))  # 可不用int,用的话时间将大幅提升


if __name__ == "__main__":
	test = Solution()
	print(test.myPow(2.0, 10))