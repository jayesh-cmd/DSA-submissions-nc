# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # Brute ---
        # arr = [] # Store the linked list in array
        # curr = head
        # while curr:
        #     arr.append(curr.val)
        #     curr = curr.next
        # left = left - 1 # 1-indexed so we will make it 0-indexed
        # right = right - 1
        # while left<right: # swap to reverse using pointers
        #     arr[left], arr[right] = arr[right], arr[left]
        #     left+=1
        #     right-=1
        # dummy = ListNode(0) # Dummy list to get linked list again
        # curr = dummy
        # for num in arr:
        #     curr.next = ListNode(num)
        #     curr = curr.next
        # return dummy.next
        # T.C. -> O(n)
        # S.C. -> O(n)

        # Optimal ---
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next

        curr = prev.next
        for _ in range(right-left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next
        # T.C. -> O(n)
        # S.C. -> O(1)