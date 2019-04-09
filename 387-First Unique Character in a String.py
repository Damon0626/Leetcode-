# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-9 下午10:19
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

'''
   1.一开始逐一元素进行count,发现超时
   2.对比，对原字符串set()再按set()中元素count，最多26次
'''


class Solution(object):
	def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		char = set(s)
		return min([s.index(c) for c in char if s.count(c)==1] or [-1])
