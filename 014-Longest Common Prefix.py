# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-31 下午6:55
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

'''
注意题目中的＂前缀＂单词
'''
class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		if not strs:
			return ""
		s1 = min(strs)  # 字母顺序a-z，充分利用了前缀的前提
		s2 = max(strs)
		for i, letter in enumerate(s1):
			if letter != s2[i]:
				return s1[:i]
		return s1

