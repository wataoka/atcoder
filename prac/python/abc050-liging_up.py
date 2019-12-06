from collections import defaultdict

def possible(flag):
    if flag:
        return False
    if N%2==0:
        for cnt in cnt_dict.values():
            if cnt != 2:
                return False
        return True
    else:
        for i, cnt in enumerate(cnt_dict.values()):
            if i==0:
                if cnt != 1:
                    return False
            else:
                if cnt != 2:
                    return False
        return True

N = int(input())
A = list(map(int, input().split()))
num = N//2

cnt_dict = defaultdict(list)

if N%2==0:
    for i in range(1, N, 2):
        cnt_dict[i] = 0
else:
    for i in range(0, N, 2):
        cnt_dict[i] = 0
for a in A:
    if not(a in cnt_dict.keys()):
        flag=False
    else:
        cnt_dict[a]+=1
        flag=True

if __name__ == "__main__":    

    if possible(flag):
        mod = 10**9+7
        res = 1
        for i in range(1, num+1):
            res = res*2%mod
        print(res)
    else:
        print(0)