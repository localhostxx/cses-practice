#include <iostream>
#include <set>
#include <vector>
using namespace std;

void permutation(vector<bool> &vis, set<string> &ans, int ansLength, int n,
                 string &currentString, string &s) {

  if (ansLength == n) {
    ans.insert(currentString);
    return;
  }

  for (int i{}; i < n; i++) {
    if (vis[i])
      continue;

    currentString.push_back(s[i]);
    vis[i] = true;
    permutation(vis, ans, ansLength + 1, n, currentString, s);
    vis[i] = false;
    currentString.pop_back();
  }

  return;
}

int main() {
  string s;
  cin >> s;

  vector<bool> vis(s.length(), false);
  set<string> ans;
  string currentString = "";
  permutation(vis, ans, 0, s.length(), currentString, s);

  cout << ans.size() << endl;
  for (string s : ans) {
    cout << s << endl;
  }

  return 0;
}
