# Implement a function to check if a linked list is a palindrome.

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def palindrome(self,head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next             #mid-point formed here

       #reverse the second half
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

       #check the first half with the second half
        while prev:
            if head.val != prev.val:
                return False
            prev = prev.next
            head = head.next
        return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print Solution().palindrome(head)
