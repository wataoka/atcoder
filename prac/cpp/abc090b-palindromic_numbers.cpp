/*
問題文
A 以上 B 以下の整数のうち、回文数となるものの個数を求めてください。 ただし、回文数とは、先頭に 0 をつけない 10 進表記を文字列として見たとき、前から読んでも後ろから読んでも同じ文字列となるような正の整数のことを指します。

制約
10000≤A≤B≤99999
入力はすべて整数である
*/

#include <iostream>

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;
  int res = 0;
  for (int i = A; i <= B; i++) {
    int s = i%10, t = i/10000%10;
    int u = i/10%10, v = i/1000%10;
    if (s==t && u==v) res++;
  }

  cout << res << endl;
}
