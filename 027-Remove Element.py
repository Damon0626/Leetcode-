# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-21 下午8:52
# @Email : wwymsn@163.com
# @Software: PyCharm


class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		while (val in nums):
			nums.remove(val)
