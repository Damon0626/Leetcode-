# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-5 下午10:01
# @Email : wwymsn@163.com
# @Software: PyCharm


class Solution:
	def fib(self, N: int) -> int:
		# 递归方法，对于层数较低1160mm
		# if N == 1:
		#     return 1
		# if N == 0:
		#     return 0
		# return self.fib(N-1) + self.fib(N-2)

		# 循环方法 48mm
		# q = 0
		# for i in range(N+1):
		#     if i == 0:
		#         p = 0
		#     elif i == 1:
		#         q = 1
		#     else:
		#         p, q = q, q+p
		# return q

		# 循环和数组  36mm
		fi = []
		for i in range(N + 1):
			if i == 0:
				fi.append(0)
			elif i == 1:
				fi.append(1)
			else:
				num = fi[i - 1] + fi[i - 2]
				fi.append(num)
		return fi[N]