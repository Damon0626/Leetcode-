# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-21 下午8:56
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array
that can make triangles if we take them as side lengths of a triangle.
'''


class Solution(object):
	def triangleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums = sorted(nums)
		count = 0
		index = len(nums) - 1

		while index > 1:
			r = index - 1
			l = 0
			while l < r:
				if nums[l] + nums[r] > nums[index]:
					count += r - l
					r -= 1
				else:
					l += 1
			index -= 1
		return count