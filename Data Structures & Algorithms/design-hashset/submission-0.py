class MyHashSet:

    def __init__(self):

        self.size = 10000

        self.buckets = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        index = self.hash(key)
        bucket = self.buckets[index]

        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)
        bucket = self.buckets[index]

        if key in bucket:
            bucket.remove(key)
        

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        bucket = self.buckets[index]

        return key in bucket
        
    # T.C. -> O(N / M)
    # S.C. -> O(M + N)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)