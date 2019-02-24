# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-24 上午11:41
# @Email : wwymsn@163.com
# @Software: PyCharm

import bisect


class Solution:
	def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
		# 方法1, 大约8800ms
		'''
		result = []
		m = k//2
		if nums == []:
			return result
		for i in range(len(nums)-k+1):
			array = sorted(nums[i:i+k])
			if k % 2:
				result.append(array[m]/1)
			else:
				result.append((array[m] + array[m - 1])/2)
		return result
		'''
		# 方法2: 利用bisect模块，参考别人提交，大约96ms
		result = []
		window = nums[:k]
		window.sort()
		isOdd = k % 2  # 判断奇偶性
		m = k // 2  # 插入的位置
		if isOdd:
			result.append(float(window[m]))
		else:
			result.append((window[m] + window[m - 1]) / 2.0)

		for i in range(k, len(nums)):
			window.pop(bisect.bisect_left(window, nums[i - k]))  # 从k到 len(nums)-k，逐个删除元素
			bisect.insort(window, nums[i]) # 在排序好的列表中，添加nums[i]在合适的位置.
			if isOdd:
				result.append(float(window[m]))
			else:
				result.append((window[m] + window[m - 1]) / 2.0)
		return result
