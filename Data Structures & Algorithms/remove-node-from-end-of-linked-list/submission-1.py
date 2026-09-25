# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Reverse
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Remove 
        head = prev
        prev = None
        curr = head
        count = 1
        while curr:
            if count == n:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                break
            prev = curr
            curr = curr.next
            count += 1

        # Reverse Back
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev