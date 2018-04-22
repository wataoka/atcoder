"""
問題文:
日本でよく使われる紙幣は、10000 円札、5000 円札、1000 円札です。以下、「お札」とはこれらのみを指します。
青橋くんが言うには、彼が祖父から受け取ったお年玉袋にはお札が N 枚入っていて、合計で Y 円だったそうですが、嘘かもしれません。このような状況がありうるか判定し、ありうる場合はお年玉袋の中身の候補を一つ見つけてください。なお、彼の祖父は十分裕福であり、お年玉袋は十分大きかったものとします。

制約:
1≤N≤2000
1000≤Y≤2×107
N は整数である。
Y は 1000 の倍数である。

入力:
入力は以下の形式で標準入力から与えられる。
N Y

出力:
N 枚のお札の合計金額が Y 円となることがありえない場合は、-1 -1 -1 と出力せよ。
N 枚のお札の合計金額が Y 円となることがありうる場合は、そのような N 枚のお札の組み合わせの一例を「10000 円札 x 枚、5000 円札 y 枚、1000 円札 z 枚」として、x、y、z を空白で区切って出力せよ。複数の可能性が考えられるときは、そのうちどれを出力してもよい。
"""

# ---------- Author: Nagata ---------- #
n, y = map(int, input().split())
for i in range(n + 1):
    for j in range(n - i + 1):
        if i * 10000 + j * 5000 + (n - i - j) * 1000 == y:
            print(i, j, n-i-j)
            exit()
print("-1 -1 -1")

# ---------- Author: Wataoka Koki ---------- #
n, y = map(int, input().split())
i, j, k = 0, 0, 0
tmp = i*10000 + j*5000 + k*1000
while tmp < 20000000:
    tmp = i*10000 + j*5000 + k*1000
    for j in range(2):
        for k in range(9):
            tmp = i*10000 + j*5000 + k*1000
            if tmp == y:
                print(i, j, k)
                exit()
    i += 1

print("-1 -1 -1")