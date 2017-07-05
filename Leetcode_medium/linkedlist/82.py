# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = pre = ListNode(0)
        root.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return root.next


from Leetcode_medium.linkedlist.linkedlist import LinkedList
s = Solution()
x = [1, 1, 2,2]

L = LinkedList(x)
L.display()
L.display(s.deleteDuplicates(L.root))