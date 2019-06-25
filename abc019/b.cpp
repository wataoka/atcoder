#include <iostream>
#include <string>

using namespace std;

int main() {
    string s, res;
    cin >> s;

    int count = 1;
    for(int i=0; i < s.length()-1; i++) {
        if(s[i] == s[i+1]) {
            count++;
        } else {
            res += s[i] + to_string(count); 
            count = 1;
        }
    }
    res += s[s.length()-1] + to_string(count); 

    cout << res << endl;
}