# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa = headA  # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def creatnode(lst):
    if lst == []:
        return None
    head = ListNode(lst[0])
    p = head
    for i in lst[1:]:
        q = ListNode(i)
        p.next = q
        p = p.next
    return head

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
    lst = []
    head = creatnode(lst)
    printlist(head)
    s.getIntersectionNode()