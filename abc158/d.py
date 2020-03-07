S = input()
Q = int(input())

num_turn = 0

front = []
end = []

for i in range(Q):
    query = input()
    if query == '1':
        num_turn += 1
    else:
        _, f, c = query.split()
        f = int(f)
        if f == 1:
            if num_turn%2==0:
                front.append(c)
            else:
                end.append(c)
        else:
            if num_turn%2==0:
                end.append(c)
            else:
                front.append(c)

S = list(S)
if num_turn%2==1:
    ans = end[::-1] + S[::-1] + front
else:
    ans = front[::-1] + S + end
print(''.join(ans))