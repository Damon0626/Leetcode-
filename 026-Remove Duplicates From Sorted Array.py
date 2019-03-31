# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-31 下午7:18
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
'''

#  需要注意的是：由于列表是可变对象的缘故，固在实例方法中也可改变对象．
#  最初的时候一直在纠结pop的方法，忘了列表是可变对象...

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		if not nums:
			return 0
		curr = 0
		for i in range(1, len(nums)):
			if nums[i] != nums[curr]:
				curr += 1
				nums[curr] = nums[i]
		return  curr+1