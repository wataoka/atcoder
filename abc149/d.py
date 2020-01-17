N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

pose2point = {
    'r': P,
    's': R,
    'p': S
}

wins = []

ans = 0
for i, pose in enumerate(T):
    if i < K:
        wins.append('win')
        ans += pose2point[pose]
    else:
        pre_pose = T[i-K]
        if wins[i-K] == 'win':
            if pose == pre_pose:
                wins.append('lose')
            else:
                wins.append('win')
                ans += pose2point[pose]
        else:
            wins.append('win')
            ans += pose2point[pose]
print(ans)