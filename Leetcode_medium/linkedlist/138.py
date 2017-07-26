# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head:
            p = ListNode(head.val)
            if head.next:
                p.next = self.copyRandomList(head.next)
            return p
        return head


from Leetcode_medium.linkedlist.linkedlist import LinkedList
s = Solution()
x = [1,2,3,4,5]

L = LinkedList(x)
L.display()
L.display(s.copyRandomList(L.root))