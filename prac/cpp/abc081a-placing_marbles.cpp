/*
問題文:
すぬけ君は1, 2, 3の番号がついた3つのマスからなるマス目を持っています。各マスには0か1が書かれており、マスiにはsiが書かれています。すぬけくんは1が書かれたマスにビー玉を置きます。ビー玉が置かれるマスがいくつあるか求めてください。

制約:
s1, s2, s3は1あるいは0

入力:
入力は以下の形式で標準入力から与えられる。
s1s2s3

出力:
答えを出力せよ。
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
  string s;
  cin >> s;
  int counter = 0;
  if (s[0] == '1') ++counter;
  if (s[1] == '1') ++counter;
  if (s[2] == '1') ++counter;
  cout << counter << endl;
}
