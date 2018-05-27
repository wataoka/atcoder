#include <cstdio>
#include <iostream>

using namespace std;

int A, B;

int main()
{
  cin >> A >> B;

  int max = A+B;

  if (A-B > max) max = A-B;
  if (A*B > max) max = A*B;


  cout << max << endl;
}
