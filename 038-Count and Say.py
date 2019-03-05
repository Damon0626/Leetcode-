# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-5 下午9:52
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
1.     1
2.     11
3.     21
4.     1211
5.     111221
'''

# my solution
class Solution:
	def countAndSay(self, n: int) -> str:
		res = '1'
		if n == 1:
			return res
		for i in range(n - 1):
			res = self.say(res)

		return res

	def say(self, x):
		counter = []
		for i in x:
			if counter == []:
				counter.append([i, 0])
			if i == counter[-1][0]:
				counter[-1][1] += 1
			else:
				counter.append([i, 1])
		return ''.join([''.join((str(i[1]), i[0])) for i in counter])
