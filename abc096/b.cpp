#include <iostream>

using namespace std;

int main() {
  int a, b, c;
  int k;

  cin >> a >> b >> c;
  cin >> k;

  bool a_flag = (a > b) && (a > c);
  bool b_flag = (b > a) && (b > c);
  bool c_flag = (c > b) && (c > a);


  int max = 0;

  if (a_flag){
    for (int i=0; i < k; i++) {
      a *= 2;
    }
  }

  if (b_flag){
    for (int i=0; i < k; i++) {
      b *= 2;
    }
  }

  if (c_flag){
    for (int i=0; i < k; i++) {
      c *= 2;
    }
  }

  cout << a+b+c << endl;

}
