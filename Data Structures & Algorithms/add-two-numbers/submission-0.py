# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # # Brute ---
        # num1 = 0 # L1 , This will convert the linked list node to numbers in reverse order
        # multi = 1
        # curr = l1
        # while curr:
        #     num1 += curr.val * multi
        #     multi *= 10
        #     curr = curr.next
        # num2 = 0 # L2
        # multi = 1
        # curr = l2
        # while curr:
        #     num2 += curr.val * multi
        #     multi *= 10
        #     curr = curr.next
        # total = num1 + num2 # Add Both Num
        # if total == 0:
        #     return ListNode(0)
        # dummy = ListNode(0) # Connect the sum in linked list in reverse order
        # curr = dummy
        # while total > 0:
        #     digit = total % 10
        #     total = total // 10
        #     curr.next = ListNode(digit)
        #     curr = curr.next
        # return dummy.next
        # # T.C. -> O(m+n)
        # # S.C. -> O(max(m,n))

        # Optimal ----
        head = ListNode(0)
        curr = head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            curr.next = ListNode(digit)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next
        # T.C. -> O(max(m,n))
        # S.C. -> O(max(m,n))