# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-5 下午9:54
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
找到列表中等于目标和的3个数
思路：
三个变量，列表首\列表尾\列表首＋１, 固定两端，移动中间．当和大于目标和，列表尾前移1位，否则中间右移１位
'''


class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		res = []
		for i in range(len(nums) - 2):
			if i > 0 and nums[i] == nums[i - 1]:
				continue  # 在=0的时候，去掉相同，其余时候相同的情况均同样处理
			l = i + 1
			r = len(nums) - 1

			while l < r:
				# print(l, r)
				s = sum([nums[i], nums[l], nums[r]])
				if s < 0:
					l += 1
				elif s > 0:
					r -= 1
				else:
					res.append([nums[i], nums[l], nums[r]])
					while (l < r) and (nums[l] == nums[l + 1]):
						l += 1
					while (l < r) and (nums[r] == nums[r - 1]):
						r -= 1
					# print(l, r)
					l += 1
					r -= 1
		return res