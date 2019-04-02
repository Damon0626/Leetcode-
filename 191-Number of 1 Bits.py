# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-2 下午9:01
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

 

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
'''


class Solution(object):
	def hammingWeight(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# 直接利用bin方法实现，时间较长
		'''
		res = bin(n)
		return res.count('1')
		'''
		# 利用右移
		'''
		count = 0
		while n!=0:
			if n & 1 == 1:
				count += 1
				n = n >> 1
			else:
				n = n>>1
		return count
		'''
		return bin(n).count('1')
