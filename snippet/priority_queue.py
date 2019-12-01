# ----- 最小値を取り出す優先度付きキュー ----- #
import heapq

a  = [1, 6, 4, 2, 6]
# heap化
heapq.heapify(a)
# 要素の挿入
heapq.heappush(a, 5)
# 最小値の取り出し
min_a = heapq.heappop(a)


# ----- 最小値を取り出す優先度付きキュー ----- #
import heapq

a = [4, 3, 5, 2, 1]
# 各要素を-1倍
a = list(map(lambda x: x*(-1), a))
# heap化
heapq.heapify(a)
# 要素の挿入
heapq.heappush(a, 7*(-1))
# 最大値の取り出し
max_a = heapq.heappop(a)*(-1)


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