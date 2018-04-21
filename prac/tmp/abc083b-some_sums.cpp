/*
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
*/


#include <iostream>
#include <typeinfo>
using namespace std;

int findSumOfDigits(int n) {
  int sum = 0;
  while (n > 0) {
    sum += n%10;
    n /= 10;
  }
  return n;
}

int main() {
  int N, A, B;
  cin >> N, A, B;
  for (int i=1; i <= N; i++) {
    int sum = findSumOfDigits(i);
    if (sum >= A && sum <= B) {
      total += i;
    }
  }

  cout << total << endl;
}
