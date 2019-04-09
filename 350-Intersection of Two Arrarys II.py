# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-9 下午10:17
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
'''


'''题干有点误解，其实是最长子数组（可以不连续，但要一个方向）'''
class Solution(object):
	def intersect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		counts = {}
		res = []
		for num in nums1:
			counts[num] = counts.get(num, 0) + 1

		for num in nums2:
			if num in counts and counts[num] > 0:
				res.append(num)
				counts[num] -= 1
		return res
