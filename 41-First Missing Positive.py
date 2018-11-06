# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-6 下午9:06
# @Email : wwymsn@163.com
# @Software: PyCharm


class Solution:
	'''
	Desc: Given an unsorted integer array, find the smallest missing positive integer.
	'''
	# method2:此方法适合没有重复的数字，先排序，然后根据坐标和值相等的关系处理
	def firstMissingPositive1(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		num.sort()
		n = len(num)
		positiveIndex = 1
		orderI = 1
		while num[positiveIndex - 1] <= 0:  # 找到正数的开始
			positiveIndex += 1
		while num[positiveIndex - 1] == orderI:
			positiveIndex += 1
			orderI += 1
			if positiveIndex > n:
				break
		return orderI

	# method1  数字最大不会超过数组的长度
	def firstMissingPositive(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		n = len(num)
		if 1 not in num or not num:  # 只要1不在数组或者数组为空，那么直接返回1
			return 1
		else:  # 否则从2开始轮询
			for i in range(2, n + 1):
				if i not in num:
					return i
			return n + 1


if __name__ == "__main__":
	num = [3, 4, -1, 1]
	test = Solution()
	print(test.firstMissingPositive(num))
