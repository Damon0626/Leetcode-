# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-2 下午8:53
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

# 在不改变数组的顺序的情况下，将所有零移到末尾
class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		# 1.需要弹出和加入
		'''
		for i in nums:
			if i == 0:
				nums.pop(nums.index(i))
				nums.append(0)
		'''
		# 2.交换位置
		zero = 0
		for i in range(len(nums)):
			if nums[i] != 0:
				nums[i], nums[zero] = nums[zero], nums[i]
				zero += 1
