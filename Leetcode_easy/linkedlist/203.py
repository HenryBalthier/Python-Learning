
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        while head.val == val:
            head = head.next
            if head == None:
                return head
        p = head
        while p.next:
            while p.next.val == val:
                p.next = p.next.next
                if p.next == None:
                    break
            p = p.next
            if p == None:
                break
        return head

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printlist(head):
    if head == None:
        print('head is None!')
        return
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
    n = 5
    for i in range(n):
        p = ListNode(i + 2)
        point.next = p
        point = p
    printlist(head)
    printlist(s.removeElements(head, 6))