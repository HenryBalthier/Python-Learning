# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        d1 = large = ListNode(-1)
        d2 = small = ListNode(0)
        cur = head

        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                large.next = cur
                large = large.next
            cur = cur.next
        large.next = None
        small.next = d1.next
        return d2.next


from Leetcode_medium.linkedlist.linkedlist import LinkedList
s = Solution()
x = [1,4,3,2,5,2]
n = 3
L = LinkedList(x)
L.display()
L.display(s.partition(L.root, n))