"""
問題文:
1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。

制約 :
1≤N≤104
1≤A≤B≤36
入力はすべて整数である

入力:
入力は以下の形式で標準入力から与えられる。
N A B

出力:
1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を出力せよ。
"""
n, a, b = map(int, input().split())

ans = 0
for i in range(1, n+1):
    if a <= sum(list(map(int, str(i)))) <= b:
        ans += i

        print(ans)
