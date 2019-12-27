class SegmentTree:

    def __init__(self, arr, segfunc=min, ide_ele=float('inf')):
        self.arr = arr
        self.segfunc = segfunc
        self.ide_ele = ide_ele

        # make self.segment tree
        self.n = len(arr)
        self.num = 2**(self.n-1).bit_length()
        self.seg = [ide_ele]*2*self.num
        self._init_seg(self.arr)

    # セグメント木を構築
    def _init_seg(self, init_val):
        for i in range(self.n):
            self.seg[i+self.num-1]=init_val[i]    
        for i in range(self.num-2,-1,-1):
            self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2]) 
        
    # k番目の値をxに変更
    def update(self, k, x):
        self.arr[k] = x
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])
        
    # 区間[p, q)に対するクエリ
    def query(self, p, q):
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = self.segfunc(res,self.seg[p])
            if q&1 == 1:
                res = self.segfunc(res,self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res,self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
        return res
    
    def get_arr(self):
        return self.arr


""" example
x = [3, 5, 2, 8, 5, 3, 4, 1, 4]

st = SegmentTree(x)
print(st.get_arr())
print(st.query(2, 5))
st.update(3, 1)
print(st.query(2, 5))
"""