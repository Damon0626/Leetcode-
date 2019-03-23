# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-23 下午8:02
# @Email : wwymsn@163.com
# @Software: PyCharm
import math
'''
本题目主要使求解二次方程的解，找到对应的关系即可解决问题
'''
# You have a total of n coins that you want to form in
# a staircase shape, where every k-th row must have exactly k coins.


class Solution:
	def arrangeCoins(self, n: int) -> int:
		return int((-1+math.sqrt(1+8*n))/2)

