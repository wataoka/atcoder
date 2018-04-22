/*
問題文:
黒板に N 個の正の整数 A1,…,AN が書かれています．
すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます．
黒板に書かれている整数すべてを，2 で割ったものに置き換える．
すぬけ君は最大で何回操作を行うことができるかを求めてください．

制約:
1≤N≤200
1≤Ai≤109

入力:
入力は以下の形式で標準入力から与えられる。
N
A1 A2 ... AN

出力:
すぬけ君は最大で何回操作を行うことができるかを出力せよ．
*/

#include <iostream>

using namespace std;

int N;
int A[210];

int main() {
  cin >> N;
  for (int i = 0; i < N; i++) cin >> A[i];

  int res = 0;

  while (true) {
    bool exist_odd = false;
    for (int i = 0; i < N; ++i) {
      if (A[i] % 2 != 0) exist_odd = true;
    }

    if (exist_odd) break;

    for (int i = 0; i < N; ++i) {
      A[i] /= 2;
    }
    ++res;
  }

  cout << res << endl;
}
