# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-24 上午10:57
# @Email : wwymsn@163.com
# @Software: PyCharm


from collections import deque


class Solution(object):
	def maxSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		# 方法1 枚举法，利用max进行查找，从头到尾进行
		"""
		result = []
		if nums == []:
			return []
		for i in range(len(nums)-k+1):
			result.append(max(nums[i:i+k]))
		return result
		"""
		# 方法2，利用双向队列
		d = deque()
		result = []
		for i in range(len(nums)):
			if d and i - d[0] == k:  # 队列不为空并且刚好等于窗的长度，之前的值就要去掉
				d.popleft()
			while d:
				if nums[d[-1]] < nums[i]:  # 去掉窗范围内的无用值
					d.pop()
				else:
					break
			d.append(i)
			if i >= k-1:
				result.append(nums[d[0]])
		return result

