# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """


from Leetcode_medium.linkedlist.linkedlist import LinkedList
s = Solution()
x = [1,None]
n = 2
L = LinkedList(x)
L.display()
L.display(s.rotateRight(L.root, n))