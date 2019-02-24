# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        new_head = jump = ListNode(0)
        new_head.next = r = l = head
        
        while True:
            count = 0
            # 找到每次反转的范围
            while r and count < k:
                r = r.next
                
                count += 1

            if count == k:
                curr, prev = l, r
                # 对k个数字进行反转
                for _ in range(k):
                    curr.next, prev, curr = prev, curr, curr.next  # 三步走 
                    # ch = curr.next
                    # curr.next = prev
                    # prev = curr
                    # curr = ch
                jump.next = prev
                jump = l
                l = r
            else:
                return new_head.next

            
        
        
        
