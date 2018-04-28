/*
  問題文
  N 人の人がいて、i 番目の人の名前は Si です。

  この中から、以下の条件を満たすように 3 人を選びたいです。

  全ての人の名前が M,A,R,C,H のどれかから始まっている
  同じ文字から始まる名前を持つ人が複数いない
  これらの条件を満たすように 3 人を選ぶ方法が何通りあるか、求めてください。ただし、選ぶ順番は考えません。

  答えが 32 bit整数型に収まらない場合に注意してください。

  制約
  1≤N≤105
  Si は英大文字からなる
  1≤|Si|≤10
  Si≠Sj(i≠j)
 */

#include <cstdio>
#include <iostream>

using namespace std;

typedef long long ll;

string s;
int N;
ll m, a, r, c, h;
ll D[5];
int P[10] = {0, 0, 0, 0, 0, 0, 1, 1, 1, 2};
int Q[10] = {1, 1, 1, 2, 2, 3, 2, 2, 3, 3};
int R[10] = {2, 3, 4, 3, 4, 4, 3, 4, 4, 4};

int main()
{
  cin >> N;
  for (int i=0; i < N; i++) {
    cin >> s;
    if(s[0] == 'M')m++;
    if(s[0] == 'A')a++;
    if(s[0] == 'R')r++;
    if(s[0] == 'C')c++;
    if(s[0] == 'H')h++;
  }
  D[0] = m, D[1] = a, D[2]=r, D[3]=c, D[4]=h;
  ll res = 0;
  for (int d=0; d < 10; d++) {
    res += D[P[d]]*D[Q[d]]*D[R[d]];
  }

  cout << res << endl;
}
