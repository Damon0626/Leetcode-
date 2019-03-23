# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-23 下午8:00
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute
the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
any combination of the coins, return -1.
'''


class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		boarder = [float('inf')] * (amount + 1)
		boarder[0] = 0

		for coin in coins:
			for amt in range(1, amount + 1):
				if amt - coin >= 0:
					boarder[amt] = min(boarder[amt], boarder[amt - coin] + 1)  # 最优子结构
		return -1 if boarder[-1] == float('inf') else boarder[-1]
