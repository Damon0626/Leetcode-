# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-2 下午8:24
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
everse bits of a given 32 bits unsigned integer.

 

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10101111110010110010011101101001.
'''


# 注意要换成32位，否则部分0丢失影响反转后整数的值
class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		bins = ''
		for i in range(32):
			bins += str(n&1)
			n = n>>1
		return int(bins, 2)


if __name__ == "__main__":
	test = Solution()
	print(test.reverseBits(43261596))
