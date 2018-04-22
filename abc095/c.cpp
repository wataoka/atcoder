#include <iostream>

using namespace std;

int main() {
  int A, B, C, X, Y;
  cin >> A >> B >> C >> X >> Y;

  int res = 0;

  if (A+B <= 2*C) {
    res = X*A + Y*B;
    cout << res;
  } else {
    if (X < Y) {
      res += C;
    }
  }
}
