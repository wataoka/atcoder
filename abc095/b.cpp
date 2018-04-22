#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int N, X;
  int m[1000] = {0};

  cin >> N >> X;
  for(int i=0; i < N; i++) cin >> m[i];

  sort(m, m + N);

  int res=0;


  for (int i=0; i < N; i++) {
    X -= m[i];
    res++;
  }

  cout << res << endl;
  res += X / m[0];

  cout << res << endl;
}
