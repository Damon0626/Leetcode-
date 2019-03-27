# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-27 下午10:31
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''


class Solution1:
	def strStr(self, haystack: str, needle: str) -> int:
		if not needle:
			return 0
		# 直接利用python自带的字符串功能可以实现
		if needle in haystack:
			return haystack.index(needle)
		else:
			return -1


class Solution2:
	def strStr(self, haystack: str, needle: str) -> int:
		# 使用循环的方法实现
		for i in range(len(haystack) - len(needle) + 1):
			if haystack[i:i + len(needle)] == needle:
				return i
		return -1
