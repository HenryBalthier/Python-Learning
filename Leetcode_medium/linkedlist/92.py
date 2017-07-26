# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m > n:
            m, n = n, m
        if m == n:
            return head

        count = 1
        p = q = head
        res = []
        while count <= n:
            if count < m:
                p = p.next
            else:
                res.append(q.val)
            if count < n:
                q = q.next
            if count == n:
                print(res)
                for i in range(len(res)):
                    p.val = res[-i-1]
                    p = p.next
            count += 1
        return head

from Leetcode_medium.linkedlist.linkedlist import LinkedList
s = Solution()
x = [1,2,3,4,5]
m = 2
n = 5
L = LinkedList(x)
L.display()
L.display(s.reverseBetween(L.root, m, n))
