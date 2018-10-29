# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-10-29 下午10:30
# @Email : wwymsn@163.com
# @Software: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# method1:每个next都相加，如果大于10，向下一个next值进1，O(N)
# method2:没想到...


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sum = node = ListNode(0)
        carryFlag = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            vSum = (v1 + v2 + carryFlag) % 10
            sum.next = ListNode(vSum)
            sum = sum.next
            carryFlag = (v1 + v2 + carryFlag)//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carryFlag:
            sum.next = ListNode(carryFlag)
        return node.next

    def addTwoNumbersDS(self, l1, l2):
        carry = 0
        head = node = ListNode('#')
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, rem = divmod(carry + val1 + val2, 10)
            node.next = ListNode(rem)
            node = node.next
            l1 = l1.next if l1 else None  # 处理尾节点时候
            l2 = l2.next if l2 else None
        if carry:  # 最后一位的进位不要忽略
            node.next = ListNode(carry)
        return head.next


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(2)
    l2 = ListNode(5)
    s.addTwoNumbersDS(l1, l2)