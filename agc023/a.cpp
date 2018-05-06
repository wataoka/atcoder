#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int N;
  long long sum[211111];

  cin >> N;
  sum[0] = 0;
  for (int i=1; i <= N; i++) {
    long long A;
    cin >> A;
    sum[i] += sum[i-1] + A;
  }

  sort(sum, sum + N + 1);

  long long l = 0;
  long long r = 0;
  long long count = 0;
  while(l <= N) {
    while(r <= N && sum[l] == sum[r]) r++;
    long long n = r - l;
    count += n*(n-1)/2;
    l = r;
  }

  cout << count << endl;

  return 0;
}
