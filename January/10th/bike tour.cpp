#include <bits/stdc++.h>

using namespace std;

int n, a[100];

void solution() {

    cin >> n;
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    for (int i = 1; i < n - 1; ++i) {
        if (a[i] > a[i-1] && a[i] > a[i+1])
            cnt++;
    }

    cout << cnt << "\n";
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solution();
    }
    return 0;
}