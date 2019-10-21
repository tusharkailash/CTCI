#Implement an algorithm to delete a node in the middle of a singly linked list,
#given only access to that node.
#EXAMPLE
#Input: the node c from the linked list a->b->c->d->e
#Result: nothing is returned, but the new linked list looks like a- >b- >d->e

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
        else:
            return "Nil"

class Solution(object):
    def deletenode(self,head, pos):
        if pos == 0:
            return head.next
        else:

            curr = head
            for i in range(pos):
                prev = curr
                curr = curr.next
            prev.next  = curr.next
        return head   

head = ListNode(7)
head.next = ListNode(1)
head.next.next = ListNode(4)
head.next.next.next = ListNode(5)
print Solution().deletenode(head,2)
