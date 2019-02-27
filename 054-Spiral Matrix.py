# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-27 下午10:24
# @Email : wwymsn@163.com
# @Software: PyCharm


# 原作者观察到的规律简直太厉害了，思路是一种，换两种方法实现．
class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		'''
			|1 2 3|	  |6 9|	  |8 7|	  |4|  =>  |5|  =>  ||
			|4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
			|7 8 9|	  |4 7|
		'''
		return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

		# 方法2
		# result = []
		# while matrix != []:
		# 	result += matrix[0]
		# 	matrix.pop(0)
		# 	# print(matrix)
		# 	matrix = [*zip(*matrix)][::-1]
		# return result
