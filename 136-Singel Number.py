# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-2 下午8:56
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''


# 采用异或的方式更简单
class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# 超时
		'''
		for i in set(nums):
			if nums.count(i) == 1:
				return i
		'''
		# 异或的方法
		res = 0
		for i in nums:
			res ^= i
		return res
