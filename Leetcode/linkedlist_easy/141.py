class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            print(None)
            return None
        p = head
        s = set()
        while p.next:
            m = id(p)
            print(m)
            if m not in s:
                s.add(m)
            else:
                return True
            p = p.next
        print(s)
        return False


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
    lst = [1,2,3,4,5,6]
    head = creatnode(lst)
    printlist(head)
    s.hasCycle(head)