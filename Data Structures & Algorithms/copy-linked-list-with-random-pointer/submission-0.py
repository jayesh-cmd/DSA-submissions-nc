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

        # # Brute --
        # if not head:
        #     return None
        # nodes = [] # Copy the nodes and store in the array
        # current = head
        # while current:
        #     new_node = Node(current.val)
        #     nodes.append(new_node)
        #     current = current.next
        # for i in range(len(nodes)-1): # connect the nodes
        #     nodes[i].next = nodes[i+1]
        # current = head # connects the random pointers
        # for i in range(len(nodes)):
        #     if current.random:
        #         target = current.random
        #         temp = head
        #         index = 0
        #         while temp != target:
        #             temp = temp.next
        #             index+=1
        #         nodes[i].random = nodes[index]
        #     else:
        #         nodes[i].random = None
        #     current = current.next
        # return nodes[0]
        # # T.C. -> O(n square) -> creating nodes, connecting nodes
        # # S.C. -> O(n) -> storing the nodes in the array

        # Optimal --
        if not head: return None

        node_map = {}
        curr = head
        while curr:
            node = Node(curr.val)
            node_map[curr] = node
            curr = curr.next

        curr = head
        while curr:
            new_node = node_map[curr]
            new_node.next = node_map[curr.next] if curr.next else None
            new_node.random = node_map[curr.random] if curr.random else None
            curr = curr.next

        return node_map[head]
        # T.C. -> O(n)
        # S.C. -> O(n)