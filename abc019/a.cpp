#include <iostream>

using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int ans;

    if (a<=b && b<=c) ans = b;  
    if (a<=c && c<=b) ans = c;
    if (b<=a && a<=c) ans = a;
    if (b<=c && c<=a) ans = c; 
    if (c<=a && a<=b) ans = a;
    if (c<=b && b<=a) ans = b;

    cout << ans << endl;
}