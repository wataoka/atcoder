#include <iostream>

using namespace std;

int main() {
  int h, w;
  cin >> h >> w;

  string s[50];

  bool ans = true;
  bool flag = false;

  for(int i=0; i < h; i++){
    for (int j=0; j < w; j++){
      if (s[i][j] == '#'){

        if ((i==0) && (j==0)) {
          if((s[i+1][j] == '.') && s[i][j+1] == '.'){
            ans = false;
            break;
          }
        }

        if (i == 0){
          if(s[i][j-1] == '.' && s[i+1][j] == '.' && s[i][j+1] == '.'){
            ans = false;
            break;
          }
          break;
        }

        if (j == 0){
          if(s[i-1][j] == '.' && s[i+1][j] == '.' && s[i][j+1] == '.'){
            ans = false;
            break;
          }
          break;
        }

        if (i == h-1){
          if(s[i][j-1] == '.' && s[i-1][j] == '.' && s[i][j+1] == '.'){
            ans = false;
            break;
          }
          break;
        }

        if (j == w-1){
          if(s[i][j-1] == '.' && s[i+1][j] == '.' && s[i-1][j] == '.'){
            ans = false;
            break;
          }
          break;
        }

        if (j == w-1){
          if(s[i][j-1] == '.' && s[i+1][j] == '.' && s[i-1][j] == '.'){
            ans = false;
            break;
          }
          break;
        }

        if(s[i-1][j] && s[i][j-1] == '.' &&  s[i+1][j] == '.' && s[i-1][j] == '.'){
          ans = false;
          break;
        }
       }

      }
    if (!(ans)){
        break;
      }
  }

  if(ans){
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

}
