# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-2 下午8:22
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

4-->5-->1-->9

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
'''
# 题目只给出一个链表中的节点，然后删除它
# 巧妙利用换值的思路


# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def deleteNode(self, node):
		"""
		:type node: ListNode
		:rtype: void Do not return anything, modify node in-place instead.
		"""
		node.val = node.next.val
		node.next = node.next.next
