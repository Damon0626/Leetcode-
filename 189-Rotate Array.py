# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-2 下午8:27
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''


class Solution(object):
	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		# 1.按照例中的分步思路，使用pop和insert方法
		'''
		for i in range(k):
			nums.insert(0, nums.pop(-1))
		'''

		# 2.利用列表加法的功能
		k = k % len(nums)
		nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

