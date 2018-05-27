#include <iostream>
#include <math.h>

using namespace std;

int A, B, C, K;

int main() {
  cin >> A >> B >> C >> K;

  int MAX = -1;
  if(A > MAX) MAX = A;
  if(B > MAX) MAX = B;
  if(C > MAX) MAX = C;

  cout << A + B + C + MAX * pow(2, K-1)  << endl;
}
