# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-15 下午10:53
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

# 按道理应该使用二分查找，这里偷懒了
class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if target not in nums:
				return -1
		return nums.index(target)  # 因该使用二分法查找才对,不过这样也可以找到...
