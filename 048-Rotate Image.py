# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-15 下午10:56
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],
'''


# 思路：首先逆序，然后做转置
class Solution(object):
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: None Do not return anything, modify matrix in-place instead.
		"""
		# 逆序
		for i in range(len(matrix) // 2):
			matrix[i], matrix[len(matrix) - i - 1] = matrix[len(matrix) - i - 1], matrix[i]

		# 转置
		for i in range(len(matrix)):
			for j in range(i, len(matrix[0])):
				if i == j:
					continue
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


