from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.q = deque()

    def get(self, key: int) -> int:
        if self.cache and key in self.cache : 
            self.q.remove(key)
            self.q.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.q.remove(key)
        elif len(self.cache) >= self.capacity:
            ele = self.q.popleft()
            del self.cache[ele]
        self.cache[key] = value
        self.q.append(key)
        # print(self.cache)
        # print(self.q)
# C = 2
#  cache : {1:1, 2:2, 3:3}
# q : [2,3]
