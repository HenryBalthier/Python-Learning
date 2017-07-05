# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        p = q = head
        while p.next:
            if n > 0:
                n -= 1
            else:
                q = q.next
            p = p.next
        if n:
            head = head.next
        else:
            q.next = q.next.next
        return head

from Leetcode_medium.linkedlist.linkedlist import LinkedList
s = Solution()
x = [1,2,3,4,5]
n = 5
L = LinkedList(x)
L.display()
L.display(s.removeNthFromEnd(L.root, n))
