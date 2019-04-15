# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-15 下午11:00
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''


# 寻找小于指定数目n的素数的个数
# 方法，首先和n一样长的数组，然后i对应的i*i一直到n，逐i个填充,肯定是i的倍数，那么肯定不是素数
class Solution(object):
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# 创建一个数组[True]*n
		if n < 3:
			return 0

		numPrime = [True] * n
		numPrime[:2] = [False] * 2
		for i in range(2, int(n ** 0.5 + 1)):
			if numPrime[i]:
				numPrime[i * i:n:i] = [False] * len(numPrime[i * i:n:i])
		return sum(numPrime)
