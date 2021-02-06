#include <iostream>

using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t; cin >> t;
    ll num;
    while (t--) {
        cin >> num;
        if (num & (num - 1)) {
            cout << "YES" << "\n";
        } else {
            cout << "NO" << "\n";
        }
    }
}