# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-2 下午8:55
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

class Solution(object):
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# 1.如果索引与当前值不一致，返回当前索引即为缺失值
		'''
		nums = sorted(nums)
		for i in range(len(nums)):
			if i != nums[i]:
				return i
		return nums[-1]+1
		'''
		# 2.利用(n^2+n)/2 - sum也可以运行
		n = len(nums)
		return ((n*(n+1))>>1) - sum(nums)
