"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # we map the old and new node in hashmap
        node_map = {None : None}

        # 1st pass - store the old and new node in hashmap
        curr = head
        while curr:
            copy = Node(curr.val)
            node_map[curr] = copy
            curr = curr.next

        # 2nd pass - now link the nodes
        curr = head
        while curr:
            copy = node_map[curr]
            copy.next = node_map[curr.next]
            copy.random = node_map[curr.random]
            curr = curr.next

        return node_map[head]