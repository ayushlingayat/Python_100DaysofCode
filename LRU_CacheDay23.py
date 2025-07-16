#Brute Approach
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []

    def get(self, key: int) -> int:
        for i, (k, v) in enumerate(self.cache):
            if k == key:
                # Move it to the end to mark as recently used
                self.cache.pop(i)
                self.cache.append((k, v))
                return v
        return -1

    def put(self, key: int, value: int) -> None:
        for i, (k, _) in enumerate(self.cache):
            if k == key:
                self.cache.pop(i)
                break
        if len(self.cache) == self.capacity:
            self.cache.pop(0)  # Remove least recently used
        self.cache.append((key, value))

# TC - O(n)
# SC -  O(capacity)


#Optimal Approach

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> node

        # Left = LRU, Right = MRU
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert a node at right (MRU side)
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove from LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# TC - O(1)
# SC - O(capacity)

