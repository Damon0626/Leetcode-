# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-24 下午9:51
# @Email : wwymsn@163.com
# @Software: PyCharm


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		minprice = float('inf')
		profit = 0
		for price in prices:
			minprice = min(price, minprice)  # 找到前向行进过程中最小值
			profit = max(profit, price - minprice)  # 找到前向行进中差值最大的值
		return profit
