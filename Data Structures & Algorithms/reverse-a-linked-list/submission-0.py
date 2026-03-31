# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Brute --
        # arr = [] # Convert The LL To Array
        # current = head
        # while current:
        #     arr.append(current.val)
        #     current = current.next
        # if not arr:
        #     return None
        # arr.reverse() # Reverse The Array
        # new_head = ListNode(arr[0]) # Convert The Array Back To Linked List
        # current = new_head
        # for i in range(1, len(arr)):
        #     current.next = ListNode(arr[i])
        #     current = current.next
        # return new_head
        # # T.C. -> O(n) - convert to array, reverse array, convert back
        # # S.C. -> O(n) - Store Arr Of n Elements

        # Optimal --
        prev = None
        current = head

        while current :
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
        # T.C. -> O(n) -> Single Pass Through Linked List
        # S.C. -> O(1) -> Only three pointers are used prev, current, next_node