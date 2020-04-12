from math import floor

N = int(input())
A = list(map(int, input().split()))

num = int(floor(N/2))

odd = []
even = []
for i in range(N):
    if i%2==0:
        even.append(A[i])
    else:
        odd.append(A[i])

ans = 0
while len(even) > num:
    even = even[:-1]

while len(odd) > num:
    odd = odd[:-1]

if len(even) == num and len(odd) == num:
    print(max(sum(even), sum(odd)))
elif len(even) == num:
    print(sum(even))
elif len(odd) == num:
    print(sum(odd))
else:
    print(sum(even))