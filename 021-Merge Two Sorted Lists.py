# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-21 下午8:50
# @Email : wwymsn@163.com
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		# 定义一个返回的节点
		d = ListNode(None)
		index = d
		while l1 and l2:
			if l1.val <= l2.val:
				index.next = l1
				l1 = l1.next
				index = index.next
			else:
				index.next = l2
				l2 = l2.next
				index = index.next

		if not l1:
			while l2:
				index.next = l2
				l2 = l2.next
				index = index.next
		elif not l2:
			while l1:
				index.next = l1
				l1 = l1.next
				index = index.next
		return d.next