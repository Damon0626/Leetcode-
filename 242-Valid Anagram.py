# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-9 下午10:12
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''


''' 字符串t是否由s片段组成'''
class Solution(object):
	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		return sorted(s) == sorted(t)  # 这种构思也是很大胆
