# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-9 下午10:15
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

	A -> 1
	B -> 2
	C -> 3
	...
	Z -> 26
	AA -> 27
	AB -> 28 
	...
Example 1:

Input: "A"
Output: 1
'''


'''可以理解为26进制'''
class Solution(object):
	def titleToNumber(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		result = 0
		s = s[::-1]
		for i in range(len(s)):
			result += (ord(s[i])-ord('A')+1)*26**i
		return result
