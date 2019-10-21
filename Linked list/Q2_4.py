# Write code to partition a linked list around a value x, such that all nodes less than
# x come before all nodes greater than or equal to x.

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val,repr(self.next))
        else:
            return "Nil"

class Solution(object):
    def partition(self,head,x):
        curr1 = dummy1 = ListNode(0)
        curr2 = dummy2 = ListNode(0)

        while head:
            if head.val < x:
                curr1.next = head
                curr1 = curr1.next
            else:
                curr2.next = head
                curr2 = curr2.next
            head = head.next
        curr2.next = None
        curr1.next = dummy2.next
        return dummy1.next


head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(10)
print Solution().partition(head,3)
