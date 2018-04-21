/*
問題文:
あなたは、500 円玉を A 枚、100 円玉を B 枚、50 円玉を C 枚持っています。 これらの硬貨の中から何枚かを選び、合計金額をちょうど X 円にする方法は何通りありますか。
同じ種類の硬貨どうしは区別できません。2 通りの硬貨の選び方は、ある種類の硬貨についてその硬貨を選ぶ枚数が異なるとき区別されます。

制約:
0≤A,B,C≤50
A+B+C≥1
50≤X≤20,000
A,B,C は整数である
X は 50 の倍数である

入力:
入力は以下の形式で標準入力から与えられる。
A
B
C
X

出力:
硬貨を選ぶ方法の個数を出力せよ。
*/

#include <iostream>
using namespace std;

int main() {
  int A, B, C, X;
  cin >> A >> B >> C >> X;
  int res = 0;
  for (int a=0; a <= A; a++) {
    for (int b=0; b <= B; b++) {
      for (int c=0; c <= C; c++) {
        int total = 500*a + 100*b + 50*c;
        if (total == X) ++res;
      }
    }
  }

  cout << res << endl;
}
