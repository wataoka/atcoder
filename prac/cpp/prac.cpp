#include <iostream>
#include <algorithm>

using namespace std;

int main(){
  int a[5] = {2, 1, 2, 4, 9};

  sort(a, a+5, greater<int>());

  for (int i=0; i<5; i++) {
    cout << a[i] << endl;
  }
}
