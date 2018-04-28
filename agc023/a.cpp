#include <iostream>

using namespace std;

int main()
{
  int N;
  int A[200001];
  int res=0;

  cin >> N;
  for(int i=0; i < N; i++) cin >> A[i];

  for (int i=0; i < N-1; i++) {
    int tmp = A[i];
    for (int j=i+1; j < N; j++) {
      tmp += A[j];
      if (tmp == 0) res++;
    }
  }

  cout << res << endl;
}
