# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p = head
        lst = []
        lst.append(p.val)
        while p.next:
            p = p.next
            lst.append(p.val)
        p = head
        l = len(lst)
        for i in range(l):
            p.val = lst[l - i - 1]
            if p.next:
                p = p.next
        printlist(head)

def printlist(head):
    p = head
    lst = []
    lst.append(p.val)
    while p.next:
        p = p.next
        lst.append(p.val)
    print(lst)

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    point = head
    n = 3
    for i in range(n):
        p = ListNode(i + 2)
        point.next = p
        point = p
    s.reverseList(head)
