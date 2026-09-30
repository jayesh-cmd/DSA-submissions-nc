class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.nxt = self.right
        self.right.prev = self.left

    def remove(self, node):
        
        before = node.prev
        after = node.nxt

        before.nxt = after
        after.prev = before

    def insert(self, node):
        before = self.right.prev

        before.nxt = node
        node.prev = before

        node.nxt = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)

        self.cache[key] = node

        self.insert(node)

        if len(self.cache) > self.capacity:

            lru = self.left.nxt

            self.remove(lru)

            del self.cache[lru.key]

        