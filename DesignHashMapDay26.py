#Brtue Approach
class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1000001  # Fixed size array

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1

# Time Complexity:
# put(), get(), remove() = O(1)
#
# Space Complexity:
# O(N) where N = 1,000,001


#Optimal Approach
class MyHashMap:
    def __init__(self):
        self.n = 10000
        self.arr = [[] for _ in range(self.n)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.n
        for i, (k, v) in enumerate(self.arr[idx]):
            if k == key:
                self.arr[idx][i] = (key, value)
                return
        self.arr[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = key % self.n
        for k, v in self.arr[idx]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.n
        self.arr[idx] = [(k, v) for k, v in self.arr[idx] if k != key]

# Time Complexity (Amortized):
# put(), get(), remove()
# O(1) on average, O(K) in worst case (K = bucket size)
# Space Complexity: O(N + M) where
# N = number of buckets (10,000), M = number of entries