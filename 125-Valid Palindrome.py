# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-6 下午9:47
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Desc: 判断是否是回文
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

'''


class Solution:
	def isPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		# method1:
		# 去掉符号，只剩字母和数字，生成数组，倒序数组，比较是否一致
		'''
		ToDo
		'''
		# method2:
		# 利用字符串的特性，比较首尾，直到最中间的那个，统一大小写
		# s[i] == s[len-i]
		if not s or len(s) == 1:
			return True
		s = s.lower()
		head = 0
		tail = len(s) - 1
		while head < tail:

			if s[head] == s[tail]:
				head += 1
				tail -= 1
			elif not s[head].isalnum():
				head += 1
			elif not s[tail].isalnum():
				tail -= 1
			else:
				return False
		return True


if __name__ == "__main__":
	s = "A man, a plan, a canal: Panama"
	test = Solution()
	test.isPalindrome()