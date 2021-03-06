# ----- 優先度付きキュークラス ----- #
import heapq

class PriorytyQueue(object):

    def __init__(self, arr, target='min'):
        self.arr = arr
        self.target = target
        self._heapify()
    
    def _heapify(self):
        if self.target == 'max':
            self.arr = list(map(lambda x:x*(-1), self.arr))
        heapq.heapify(self.arr)
    
    def push(self, x):
        if self.target == 'max':
            x *= -1
        heapq.heappush(self.arr, x)

    def pop(self):
        res = heapq.heappop(self.arr)
        if self.target == 'max':
            return res*(-1)
        else:
            return res
    
    def get_arr(self):
        if self.target == 'max':
            return list(map(lambda x:x*(-1), self.arr))
        else:
            return self.arr
    
    def is_empty(self):
        return len(self.arr) == 0

N, M = map(int, input().split())
A = list(map(int, input().split()))
pq = PriorytyQueue(A, target='max')

for i in range(M):
    max_value = pq.pop()
    pq.push(max_value//2)

print(sum(pq.get_arr()))