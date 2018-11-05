# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-5 下午11:00
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
题目描述：
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output
“Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
'''


class Solution:
	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		# method1:

		result = []
		for i in range(n):
			if (i+1)%3 == 0 and (i+1)%5 == 0:
				result.append('FizzBuzz')
			elif (i+1)%3 == 0:
				result.append('Fizz')
			elif (i+1)%5 ==0:
				result.append('Buzz')
			else:
				result.append(str(i+1))
		return result

		# method2:改进方法1

		result = []
		for i in range(1, n+1):
			if i % 15 == 0:
				result.append('FizzBuzz')
			elif i % 3 == 0:
				result.append('Fizz')
			elif i % 5 ==0:
				result.append('Buzz')
			else:
				result.append(str(i))
		return result

		# method3:考虑到字符串也是可以相乘的

		return ['Fizz' * (not (i % 3)) + 'Buzz' * (not (i % 5)) or str(i) for i in range(1, n + 1)]


if __name__ == "__main__":
	test = Solution()
	test.fizzBuzz(15)