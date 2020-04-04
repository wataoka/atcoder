n, k = map(int, input().split())
can = n%k
print(min(abs(can-k), abs(k-can), can))