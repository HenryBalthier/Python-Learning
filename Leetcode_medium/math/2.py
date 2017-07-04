# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = res = ListNode(0)
        while l1 or l2 or c:
            if l1 == None and l2 == None:
                if c == 1:
                    res = ListNode(1)
            elif l1 == None:
                l1 = ListNode(0)
            elif l2 == None:
                l2 = ListNode(0)
            r, c = (l1.val + l2.val + c) % 10, (l1.val + l2.val + c) // 10
            res.next = ListNode(r)
            l1, l2, res = l1.next, l2.next, res.next

        return root.next
