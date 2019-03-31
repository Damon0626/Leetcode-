# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-31 下午8:56
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

# 对比3种方法，循环每个元素的方法较为省时间．
class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		# 两种方法
		# 1.转换成实数计算
		'''
		nums = 0
		for i in range(len(digits)):
			nums += digits[i]*10**(len(digits)-1-i)
		return [int(i) for i in str(nums+1)]	
		'''
		# 2.递归方法
		'''
		if not digits:
			digits = [1]
		elif digits[-1] == 9:
			digits = self.plusOne(digits[:-1])
			digits.extend([0])
		else:
			digits[-1] += 1
		return digits
		'''
		# 3.循环方法
		for i in range(len(digits)-1, -1, -1):
			if digits[i] != 9:
				digits[i] += 1
				return digits
			digits[i] = 0
		return [1]+digits
