n = int(input())

x = []
for i in range(1, 10):
    for j in range(1, 10):
        x.append(i*j)

if n in x:
    print("Yes")
else:
    print("No")