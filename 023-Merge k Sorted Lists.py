# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-27 下午10:22
# @Email : wwymsn@163.com
# @Software: PyCharm


# Definition for singly-linked list.
# class ListNode:
#	 def __init__(self, x):
#		 self.val = x
#		 self.next = None


# 有点投机取巧的感觉
class Solution:
	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		res = []
		for i in lists:
			while i:
				res.append(i.val)
				i = i.next
		return sorted(res)
