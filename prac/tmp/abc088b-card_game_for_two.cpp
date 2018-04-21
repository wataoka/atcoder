/*
  問題文:
  N 枚のカードがあります. i 枚目のカードには, ai という数が書かれています.
  Alice と Bob は, これらのカードを使ってゲームを行います. ゲームでは, Alice と Bob が交互に 1 枚ずつカードを取っていきます. Alice が先にカードを取ります.
  2 人がすべてのカードを取ったときゲームは終了し, 取ったカードの数の合計がその人の得点になります. 2 人とも自分の得点を最大化するように最適な戦略を取った時, Alice は Bob より何点多く取るか求めてください.

  制約:
  N は 1 以上 100 以下の整数
  ai (1≤i≤N) は 1 以上 100 以下の整数

  入力:
  入力は以下の形式で標準入力から与えられる.
  N
  a1 a2 a3 … aN

  出力:
  両者が最適な戦略を取った時, Alice は Bob より何点多く取るかを出力してください

*/

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  int N;
  int a[100];
  cin >> N;
  for (int i = 0; i < N; ++i) cin >> a[i];

  sort(a, a+N, greater<int>());

  for (int i=0; i < N; ++i) {
    if (i%2 == 0) {
      Alice += a[i];
    } else {
      Bob += a[i];
    }
  }
  cout << Alice - Bob << endl;

}
