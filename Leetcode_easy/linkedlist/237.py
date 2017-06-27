# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        count = 1
        while p.next:
            count += 1
            if count == 3:
                p.next = p.next.next
            p = p.next


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    point = head
    n = 3
    for i in range(n):
        p = ListNode(i+2)
        point.next = p
        point = p

    s.deleteNode(head)