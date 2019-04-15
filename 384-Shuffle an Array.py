# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-15 下午10:58
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
'''
# 题目考虑淋可变数据类型在实例方法中的改变对实际结果的影响
import random


class Solution(object):

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		# self.reset = lambda: nums
		# self.shuffle = lambda: random.sample(nums, len(nums))
		self.nums = nums

	def reset(self):
		"""
		Resets the array to its original configuration and return it.
		:rtype: List[int]
		"""
		return self.nums

	def shuffle(self):
		"""
		Returns a random shuffling of the array.
		:rtype: List[int]
		"""
		ans = self.nums[:]  # 拷贝一份
		random.shuffle(ans)
		return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()