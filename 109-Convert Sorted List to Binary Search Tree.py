# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-25 下午10:33
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
将链表转换为二叉搜索树，先找到root根节点
然后递归进行左子树和右子树的创建．
'''
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def sortedListToBST(self, head: ListNode) -> TreeNode:
		if not head:
			return None
		if not head.next:
			return TreeNode(head.val)
		slow, fast = head, head.next.next
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
		tmp = slow.next  # 链表中间值，即root
		slow.next = None
		root = TreeNode(tmp.val)
		root.left = self.sortedListToBST(head)
		root.right = self.sortedListToBST(tmp.next)

		return root
