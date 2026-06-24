import heapq

class MinStack:

    def __init__(self):
        self.lazy_deletion = {}
        self.pq = []
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        heapq.heappush(self.pq, val)

    def pop(self) -> None:
        val = self.s.pop()
        self.lazy_deletion[val] = self.lazy_deletion.get(val, 0) + 1

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        while self.pq and self.lazy_deletion.get(self.pq[0], 0) > 0:
            val = heapq.heappop(self.pq)
            self.lazy_deletion[val] -= 1

            if self.lazy_deletion[val] == 0:
                del self.lazy_deletion[val]

        return self.pq[0]