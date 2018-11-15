# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-4 下午10:53
# @Email : wwymsn@163.com
# @Software: PyCharm

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        if x < 0:
            return 0
        else:
            return int(x**0.5)
        """
        if x < 2:
            return x
        else:
            # 二分查找
            low = 0
            high = x
            while(low<high):
                mid = (low + high)//2
                if x/mid >= mid:
                    low = mid + 1
                else:
                    high = mid
            return low-1


if __name__ == "__main__":
    test = Solution()
    print(test.mySqrt(8))