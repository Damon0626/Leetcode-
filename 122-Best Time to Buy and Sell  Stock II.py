# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-24 下午9:52
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
贪心算法
'''
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		# 贪心算法
		profit = 0
		for i in range(len(prices)-1):
			if prices[i+1] > prices[i]:
				profit += prices[i+1] - prices[i]
		return profit