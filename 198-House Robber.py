# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-24 下午9:47
# @Email : wwymsn@163.com
# @Software: PyCharm
'''
You are a professional robber planning to rob houses along a street. Each house has a
 certain amount of money stashed, the only constraint stopping you from robbing each
 of them is that adjacent houses have security system connected and it will automatically
 contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
'''

'''
由于不能偷临近的房子，所以分两种情况1)偷当前房子，那么最大价值为dp[i-2]+num[i]
                              2)不偷当前房子，最大价值为dp[i-1]
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # prev1 = prev2 = 0
        # for num in nums:
        #     temp = prev1
        #     prev1 = max(prev2+num, prev1)
        #     prev2 = temp
        # return prev1
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]