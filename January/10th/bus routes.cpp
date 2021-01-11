#include <bits/stdc++.h>

using namespace std;
using ll = long long;

ll n, d, a[1000];

void solution() {
    cin >> n >> d;
    for (int i = 0; i < n; ++i)
        cin >> a[i];
    
    ll low = 1, high = d;
    ll ans = 1;
    while (low <= high) {
        ll mid = (high - low) / 2 + low;
        ll minVal = mid;
        for (int i = 0; i < n; ++i) {
            minVal = (ceil(minVal / (double)a[i]) * a[i]);
            if (minVal > d) {
                minVal = -1;
                break;
            }
        }

        if (minVal == -1) {
            high = mid-1;
        } else {
            ans = mid;
            low = mid+1;
        }
    }

    cout << ans << "\n";
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