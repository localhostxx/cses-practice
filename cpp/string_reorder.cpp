#include <iostream>
#include <vector>
using namespace std;

int main() {
  string s;
  cin >> s;

  vector<int> freqMap(26, 0);
  for (auto const c : s) {
    freqMap[c - 'A']++;
  }

  string ans;

  for (int i{}; i < 26; i++) {
  }

  return 0;
}
