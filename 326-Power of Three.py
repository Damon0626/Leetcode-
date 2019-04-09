# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-9 下午10:23
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
'''
'''发现math.log(243, 3)结果不对'''


class Solution(object):
	def isPowerOfThree(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		# if n <= 0:
		# 	return False
		# while n % 3 == 0:
		# 	n = n / 3
		# return True if n == 1 else False

		# 2.第二种方法, 因为int最长为32位，其中3的最大次幂为19
		return n >= 0 and 3**19 % n == 0
