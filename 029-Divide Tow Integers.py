# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-21 下午8:53
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.
'''


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 超时
        '''
        i = 0
        p, q = abs(dividend), abs(divisor)
        if q == 0:
            return -1
        while p >= q:
            p -= q
            i += 1
        if (dividend < 0 and divisor < 0) or (dividend >0 and divisor > 0):
            return i
        else:
            return -i
        '''
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)