def remaining(s1, s2):
    if not("R" in [s1, s2]):
        return "R"
    elif not("B" in [s1, s2]): 
        return "B"
    else:
        return "G"

N = int(input())
S = list(input())

num_R = [0 for _ in range(N)]
num_G = [0 for _ in range(N)]
num_B = [0 for _ in range(N)]
if S[-1] == "R":
    num_R[-1] = 1
elif S[-1] == "B":
    num_B[-1] = 1
else:
    num_G[-1] = 1

for i in range(N-2, -1, -1): 
    if S[i]=="R":
        num_R[i] = num_R[i+1]+1
        num_G[i] = num_G[i+1]
        num_B[i] = num_B[i+1]
    elif S[i]=="G":
        num_R[i] = num_R[i+1]
        num_G[i] = num_G[i+1]+1
        num_B[i] = num_B[i+1]
    else:
        num_R[i] = num_R[i+1]
        num_G[i] = num_G[i+1]
        num_B[i] = num_B[i+1]+1

if __name__ == "__main__":
    ans = 0
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            if S[i] == S[j]:
                continue
            target = remaining(S[i], S[j])
            if target == 'R':
                num = num_R
            elif target == 'G':
                num = num_G
            else:
                num = num_B

            ans += num[j+1]
            if j+(j-i) < N:
                if S[j+(j-i)]==target:
                    ans -= 1
    print(ans)