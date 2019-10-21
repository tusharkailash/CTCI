# Given a circular linked list, implement an algorithm which returns the node at
# the beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points
# to an earlier node, so as to make a loop in the linked list.
# EXAMPLE
# Input: A - > B - > C - > D - > E - > C [the same C as earlier]
# Output: C



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val,repr(self.next))
        else:
            return "Nil"

class Solution(object):
    def circular(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                fast = head
                while slow!=fast:
                    slow = slow.next
                    fast = fast.next
                return fast
        return None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(3)
print Solution().circular(head)
