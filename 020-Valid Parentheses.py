# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-12 下午9:58
# @Email : wwymsn@163.com
# @Software: PyCharm


'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''


class Solution:
	def isValid1(self, s):  # 将(){}[]全部替换掉，重复执行
		"""
		:type s: str
		:rtype: bool
		"""
		while len(s)>0:
			if "[]" in s or "()" in s or "{}" in s:
				s = s.replace("()", "").replace("[]", "").replace("{}", "")
			else:
				return False

		if not s:
			return True
	
	def isValid2(self):
		# method2：仿照堆栈的方法；
		if len(s) %2:
			return False
		stack = []
		for i in s:
			if i == "(" or i == "{" or i == "[":
				stack.append(i)
			else:
				if i == ")":
					if not stack or stack[-1] != "(":
						return False
					else:
						stack.pop()
				if i == "]":
					if not stack or stack[-1] != "[":
						return False
					else:
						stack.pop()
				if i == "}":
					if not stack or stack[-1] != "{":
						return False
					else:
						stack.pop()
		if not stack:
			return True
		else:
			return False


if __name__ == "__main__":
	s = ""
	test = Solution()
	print(test.isValid(s))