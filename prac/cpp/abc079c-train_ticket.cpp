/*
  問題文
  駅の待合室に座っているjoisinoお姉ちゃんは、切符を眺めています。

  切符には 4 つの 0 以上 9 以下の整数 A,B,C,D が整理番号としてこの順に書かれています。

  A op1 B op2 C op3 D = 7 となるように、op1,op2,op3 に + か - を入れて式を作って下さい。

  なお、答えが存在しない入力は与えられず、また答えが複数存在する場合はどれを出力してもよいものとします。

  制約
  0≦A,B,C,D≦9
  入力は整数からなる
  答えが存在しない入力は与えられない

*/

#include <cstdio>
char s[5];
int main()
{
  scanf ("% s " ,& s );
  int a = s [0] - ’0 ’ , b = s [1] - ’0 ’ , c = s [2] - ’0 ’ , d = s [3] - ’0 ’;
  if (a -b -c - d ==7) printf ("% d -% d -% d -% d =7\ n " ,a ,b ,c , d );
  else if (a -b - c + d ==7) printf ("% d -% d -% d +% d =7\ n " ,a ,b ,c , d );
  else if (a - b +c - d ==7) printf ("% d -% d +% d -% d =7\ n " ,a ,b ,c , d );
  else if (a - b + c + d ==7) printf ("% d -% d +% d +% d =7\ n " ,a ,b ,c , d );
  else if ( a +b -c - d ==7) printf ("% d +% d -% d -% d =7\ n " ,a ,b ,c , d );
  else if ( a +b - c + d ==7) printf ("% d +% d -% d +% d =7\ n " ,a ,b ,c , d );
  else if ( a + b +c - d ==7) printf ("% d +% d +% d -% d =7\ n " ,a ,b ,c , d );
  else if ( a + b + c + d ==7) printf ("% d +% d +% d +% d =7\ n " ,a ,b ,c , d );
}
