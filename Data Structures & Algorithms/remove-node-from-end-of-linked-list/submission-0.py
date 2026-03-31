# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # # Brute --
        # if not head:
        #     return None

        # length = 0
        # curr = head
        # while curr:
        #     length += 1
        #     curr = curr.next

        # position_from_start = length - n # Gives index to remove
        
        # if position_from_start == 0:
        #     return head.next
        
        # curr = head
        # for _ in range (position_from_start - 1):
        #     curr = curr.next

        # curr.next = curr.next.next
        # return head
        # # T.C. -> O(n) -> find length, traverse to position
        # # S.C. -> O(1) -> No extra space used

        # Optimal --
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
        # T.C. -> O(n) -> Single pass through list
        # S.C. -> O(1) -> only two pointers