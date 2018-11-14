# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-13 下午10:10
# @Email : wwymsn@163.com
# @Software: PyCharm


class Solution:
	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		#  method1:方法很简洁，但是这个关系我还没看懂.....
		dp, stack = [0] * (len(s) + 1), []
		for i in range(len(s)):
			if s[i] == '(':
				stack.append(i)
			else:
				if stack:
					p = stack.pop()
					dp[i + 1] = dp[p] + i - p + 1
		return max(dp)


if __name__ == "__main__":
	s = "()(()"
	test = Solution()
	print(test.longestValidParentheses(s))