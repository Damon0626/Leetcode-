# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-18 下午9:53
# @Email : wwymsn@163.com
# @Software: PyCharm


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
原理：
首先判定链表有环才能进行链表环起始点的确认，否则直接返回None;
当快慢指针相遇的时候，假设快\慢指针位于点M, 链表环起始点为N, 链表起始点为O,
那么此时快指针走的路程： O-->N-->M-->N-->M;
		慢指针的路程： O-->N-->M;
又因为快指针使慢指针路程的2倍，可以得到M-->N = O-->N，即相遇点到链表环起始点与链表头节点到链表环起始点距离相等;
所以：
当快慢指针相遇的时候，将慢指针slow重新指回链表开头，逐个往后，即可返回链表环起始点．
'''


class Solution(object):
	def detectCycle(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next:
			return None
		fast = head
		slow = head

		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next

			if slow == fast:
				slow = head

				while (slow != fast):
					slow = slow.next
					fast = fast.next
				return slow
			else:
				continue
		return None