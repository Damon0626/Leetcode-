# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-23 下午8:04
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
You are given coins of different denominations and a total amount of money.
 Write a function to compute the number of combinations that make up that amount.
 You may assume that you have infinite number of each kind of coin.
'''


class Solution:
	def change(self, amount: int, coins: List[int]) -> int:
		nums = [0]*(amount+1)
		nums[0] = 1
		for coin in coins:
			for i in range(1, amount+1):
				if i-coin >= 0:
					nums[i] += nums[i-coin]  # 最优子结构，找到这层关系，DP问题即可得到思路解决
		return nums[-1]
