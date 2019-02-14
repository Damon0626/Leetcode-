# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-14 下午10:02
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
判断链表中是否有环：
思路：常规解法－＞快慢指针
	如果有环，那么终归是要相遇的;
	如果没有环，只要快指针到链表位即可，此时有两种可能，奇数和偶数长度，保证q.next和q.next.next都不是None,就可以了．
'''


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def hasCycle(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if not head or not head.next:  # 判空和单节点链表
			return False
		p = head
		q = head

		while q.next and q.next.next:
			q = q.next.next
			p = p.next
			if p == q:
				return True
			else:
				continue
		return False
