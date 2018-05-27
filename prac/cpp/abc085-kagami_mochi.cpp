#include <cstdio>
#include <string>
#include <iostream>
#include <cmath>
#include <vector>
#include <stack>

using namespace std;

int main(void) {
  int N, d, cnt=0;
  unsigned int i;

  vector<int> mochi;

  cin >> N;

  mochi.resize(N);

  while (N--) {
    cin >> d;
    for (i=0; i < mochi.size(); i++) {
      if (d == mochi[i]) break;
    }
    if (i == mochi.size()) {
      mochi.push_back(d);
      cnt++;
    }
  }

  cout << cnt << endl;
  return 0;
}
