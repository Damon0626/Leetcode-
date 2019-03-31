# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-31 下午9:20
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''



class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		# 1.DP的思路不要再好
		'''
		for i in range(1, len(nums)):
			if nums[i-1] >= 0:
				nums[i] += nums[i-1]
		return max(nums)
		'''

		# 2.sliding window
		if len(nums) < 1:
			return sum(nums)

		cursum = 0
		maxsum = float("-inf")
		for i in range(len(nums)):
			if cursum <= 0:
				cursum = nums[i]
			else:
				cursum += nums[i]

			if cursum > maxsum:
				maxsum = cursum
		return maxsum