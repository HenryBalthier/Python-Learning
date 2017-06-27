# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        p = head
        lst = []
        lst.append(p.val)
        print(p.val)
        while p.next:
            p = p.next
            lst.append(p.val)
            print(p.val)
        return lst == lst[::-1]


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    point = head
    n = 3
    for i in range(n):
        p = ListNode(i + 2)
        point.next = p
        point = p
    for i in range(4):
        p = ListNode(4 - i)
        point.next = p
        point = p
    print(s.isPalindrome(head))