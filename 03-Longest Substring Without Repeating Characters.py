# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-10-29 下午9:54
# @Email : wwymsn@163.com
# @Software: PyCharm


class Solution:
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		# 想法：建立一个队列[],如果新进入的值和之前的重复了，那么将原队列中重复的值出列，从下一个值开始算起
		if not s:
			return 0
		window = []
		history = [0]
		for i in range(len(s)):
			while (s[i] in window):
				window.pop(0)
			window.append(s[i])
			history.append(len(window))
		return max(history)


	def lengthofLongestSubstringDS(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		start = maxLength = 0
		usedChar = {}

		for i in range(len(s)):
			if s[i] in usedChar and start <= usedChar[s[i]]:  # 开始计算长度的起始点参与后面最大长度的计算
				start = usedChar[s[i]] + 1
			else:
				maxLength = max(maxLength, i - start + 1)

			usedChar[s[i]] = i

		return maxLength


if __name__ == "__main__":
	test = Solution()
	test.lengthofLongestSubstringDS("tmmzuxt")