/*
  問題文:
  シカのAtCoDeer君は二つの正整数 a, bを見つけました。　aとbの積が偶数か奇数か判定してください。

  制約:
  1 ≤ a,b ≤ 10000
  a,b は整数

  入力:
  入力は以下の形式で標準入力から与えられる。
  a b

  出力:
  積が奇数なら Odd と、 偶数なら Even と出力せよ。
*/

#include <iostream>

using namespace std;

int main(){
  int a, b;
  cin >> a >> b;
  int c = a*b;
  if (c % 2 == 0) cout << "Even" << endl;
  else cout << "Odd" << endl;
}
