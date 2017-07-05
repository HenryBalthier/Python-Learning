# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p = head
        pre = None
        while p.next:
            q = p.next
            if not pre:
                p.next, q.next = q.next, p
                head = q
            else:
                pre.next, p.next, q.next = q, q.next, p
            pre = p
            if p.next:
                p = p.next
            else:
                break
        return head

from Leetcode_medium.linkedlist.linkedlist import LinkedList
s = Solution()
x = [1,2]

L = LinkedList(x)
L.display()
L.display(s.swapPairs(L.root))
