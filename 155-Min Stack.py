# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-4-15 下午11:06
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();	  --> Returns 0.
minStack.getMin();   --> Returns -2.
'''


class MinStack(object):

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stack = []
		self.minstack = []

	def push(self, x):
		"""
		:type x: int
		:rtype: None
		"""
		self.stack.append(x)
		if len(self.minstack) == 0:
			self.minstack.append(x)
		else:
			if self.minstack[-1] >= x:
				self.minstack.append(x)

	def pop(self):
		"""
		:rtype: None
		"""
		if len(self.stack) == 0:
			return None
		if self.top() == self.minstack[-1]:
			self.minstack.pop()
		self.stack.pop()

	def top(self):
		"""
		:rtype: int
		"""
		return self.stack[-1]

	def getMin(self):
		"""
		:rtype: int
		"""
		return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()