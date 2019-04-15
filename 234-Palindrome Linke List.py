# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-15 下午11:03
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''


# 判断一个链表是不是回文性质
# 从中间开始，将前半部分或者后半部分进行反转，然后在比较是否一致，如果一致则回文，否则不
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		# 首先找到中间结点，然后将后半部分反转，然后逐个比较
		# 1.找到中间结点
		fast = head
		slow = head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next

		# 2.反转后半部分
		node = None
		while slow:
			# nxt = slow.next
			# slow.next = node
			# node=slow
			# slow = nxt
			slow.next, node, slow = node, slow, slow.next

		# 3逐项判断
		while node and head:
			if node.val != head.val:
				return False
			node = node.next
			head = head.next
		return True
