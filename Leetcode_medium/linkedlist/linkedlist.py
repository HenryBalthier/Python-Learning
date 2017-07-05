# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def __init__(self, lst):
        self.root = p = ListNode(lst[0])
        for i in range(len(lst)):
            if i == 0:
                continue
            p.next = ListNode(lst[i])
            p = p.next

    def display(self, p=None):
        if p == None:
            p = self.root
        lst = []
        lst.append(p.val)
        while p.next:
            p = p.next
            lst.append(p.val)
        print(lst)

if __name__ == '__main__':
    x = [1,2,3,4,5,6,7]
    L = LinkedList(x)
    print(L.root.val)
    L.display()