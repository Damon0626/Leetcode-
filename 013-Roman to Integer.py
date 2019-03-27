# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-27 下午10:34
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
将罗马数字转换为阿拉伯数字
介绍：
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol	   Value
I			 1
V			 5
X			 10
L			 50
C			 100
D			 500
M			 1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
'''

# 重点找到加减的条件，即：小数在前大数在后，执行减法，否则执行加法．
class Solution:
	def romanToInt(self, s: str) -> int:
		roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
		result = 0
		# 重点找到减法之间的关系，是个叠加或者叠减的过程
		for i in range(len(s)-1):
			if roman[s[i]] < roman[s[i+1]]:
				result -= roman[s[i]]
			else:
				result += roman[s[i]]
		return result + roman[s[-1]]
