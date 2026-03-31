# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Brute --
        # if not head or not head.next:
        #     return 

        # nodes = []
        # current = head
        # while current:
        #     nodes.append(current)
        #     current = current.next

        # left = 0
        # right = len(nodes)-1

        # while left < right:
        #     nodes[left].next = nodes[right]
        #     left+=1
        #     if left == right:
        #         break
        #     nodes[right].next = nodes[left]
        #     right-=1
        # nodes[left].next = None
        # T.C. -> O(n) -> We iterate through the linked list once to create the array (taking $N$ steps). Then, we iterate through the array once using the two pointers 
        # S.C. -> O(n) -> We are storing every single node inside a Python list (nodes).

        # Optimal --
        if not head:
            return 
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first, second = temp1, temp2
        # T.C. -> O(n) -> Middle, Reverse, Merging
        # S.C. -> O(1) -> No extra space used to store nodes like brute force method