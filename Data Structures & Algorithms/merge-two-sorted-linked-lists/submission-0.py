# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Brute --
        # values = []
        # curr = list1
        # while curr:
        #     values.append(curr.val)
        #     curr = curr.next
        # curr = list2
        # while curr:
        #     values.append(curr.val)
        #     curr = curr.next
        # values.sort()
        # dummy = ListNode(0)
        # current = dummy
        # for val in values:
        #     current.next = ListNode(val)
        #     current = current.next
        # return dummy.next
        # T.C. -> O(m+n) -> m is the len of list1 and n is len of list2
        # S.C. -> O(m+n) -> storing array, linked list

        # Optimal --
        dummy = ListNode(0)
        current = dummy

        ptr1, ptr2 = list1, list2

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                current.next = ptr1
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2 = ptr2.next
            current = current.next
        if ptr1:
            current.next = ptr1
        else:
            current.next = ptr2

        return dummy.next
        # T.C. -> O(m+n) -> process each node from both lists
        # S.C. -> O(1) -> No Extra Space Used