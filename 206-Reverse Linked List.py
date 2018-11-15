# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-15 下午10:23
# @Email : wwymsn@163.com
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def reverseList1(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		# method1:类似堆栈，省去逐个pop的过程，每次循环直接在首位插入
		order = []
		if not head:
			return head
		p = head
		while p:
			order.insert(0, p.val)
			p = p.next
		return order

	def reverseList(self, head):  # 将首位和其余为看作是A, B两个部分，将A放在B后，指向None;B的首个元素命名为A,重复
		if not head:
			return head
		curr = head
		prev = None
		while curr:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
			if not curr:
				return prev  # 此时的头节点


if __name__ == "__main__":
	s = [1, 2, 3, 4, 5]
	i = 0
	head = None
	while i < len(s):
		if not head:
			head = ListNode(s[i])
			p = head
		else:
			p.next = ListNode(s[i])
			p = p.next
		i += 1

	test = Solution()
	print(test.reverseList(head))
