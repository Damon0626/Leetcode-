# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-20 下午10:14
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Given a 32-bit signed integer, reverse digits of an integer.
'''


class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		reverse = []
		result = 0
		x_abs = abs(x)

		while x_abs != 0:
			tail = x_abs % 10
			x_abs = x_abs // 10
			reverse.append(tail)
		index = len(reverse) - 1
		for i in reverse:
			result += i * (10 ** index)
			index -= 1

		if (result <= -(2 ** 31)) or (result > (2 ** 31 - 1)):
			return 0
		else:
			if x < 0:
				return - result
			else:
				return result

	def reverseByNetFriend(self, x):
		result = 0
		x_abs = abs(x)
		while x_abs != 0:
			result = result * 10 + x_abs % 10
			x_abs = x_abs // 10
		if (result <= -(2 ** 31)) or (result > (2 ** 31 - 1)):
			return 0
		else:
			return - result if x < 0 else result


if __name__ == "__main__":
	test = Solution()
	x = -12345678
	print(test.reverseByNetFriend(x))
