# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-5 下午9:58
# @Email : wwymsn@163.com
# @Software: PyCharm


'''
不允许使用＇＋／－＇计算两个数的和
采用二进制的异或和与
'''


class Solution:
	def getSum(self, a: int, b: int) -> int:
		# 方法1 递归，深度太大，报错
		# if b == 0:
		#     return a
		# s = a ^ b
		# c = (a & b) << 1
		# self.getSum(s, c)

		# 方法2
		# return sum([a, b])

		ta = a & b
		tb = a ^ b
		while (ta):
			t_a = tb
			t_b = ta << 1
			ta = t_a & t_b
			tb = t_a ^ t_b
		return tb
