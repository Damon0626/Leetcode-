# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-2 下午8:29
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


# 用一个集合记录每次计算的结果．最终1的所有次计算都是1.
# 对于不是Happy Number的话，记录每次计算的值，如果曾经出现过，计算结果陷入死循环，可知不是Happer Number
class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		memo = set()
		while n != 1:
			n = sum(int(i)*int(i) for i in str(n))
			if n in memo:
				return False
			memo.add(n)
		return True
