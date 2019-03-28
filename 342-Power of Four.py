'''Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?'''

import mat

h
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # 首先0不是4的倍数，去除
        # 然后num&(num-1)确定是2的倍数
        # 是2的倍数，不一定是4的倍数，在与“10101010101010101010101010101010”去掉纯2的倍数的值
        return num != 0 and num &(num-1) == 0 and num & 1431655765== num
