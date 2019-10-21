#Implement an algorithm to find the kth to last element of a singly linked list.

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val,repr(self.next))
        else:
            return 'Nil'

class Solution(object):
    def kth_to_last(slef,head,k):
        p1 = p2 = head
        for i in range(k):
            p2 = p2.next

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        return p1.val



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print Solution().kth_to_last(head,2)
