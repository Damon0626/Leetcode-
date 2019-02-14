# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-14 下午7:20
# @Email : wwymsn@163.com
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def swapPairs(self, head):  # pre->a->b->b.next  ==> pre->b->a->b.next && pre = a
		pre, pre.next = self, head
		while pre.next and pre.next.next:
			a = pre.next
			b = a.next
			pre.next, b.next, a.next = b, a, b.next
			pre = a
		return self.next

	def swapPairsWithRecursively(self, head):
		if head and head.next:
			tmp = head.next
			head.next = self.swapPairsWithRecursively(tmp.next)
			tmp.next = head
			return tmp
		return head


if __name__ == "__main__":
	s = [1, 2, 3, 4]
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
	h = test.swapPairsWithRecursively(head)
	while h:
		print(h.val, end=' ')
		h = h.next
