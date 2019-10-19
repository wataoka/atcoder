#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<long long> val;

int main() {
    while (cin >> N) {
        val.resize(N);
        for (int i = 0; i < N; ++i) cin >> val[i];
        sort(val.begin(), val.end());
        bool ok = false;
        for (int i = 0; i < N-2; ++i) {
            if (val[i + 2] < val[i] + val[i+1]) ok = true;
        }
        if (ok) cout << "possible" << endl;
        else cout << "impossible" << endl;
    }
}