#include <iostream>

using namespace std;

class Neko{
private:
  string name;
public:
  Neko(string s) {
    name = s;
  }
  void naku() {
    cout << "にゃあ。俺様は" << name << "だ" << endl;
  }
};

int main(){
  Neko dora("ボス");
  dora.naku();
}
