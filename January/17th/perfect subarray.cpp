#include <bits/stdc++.h>
using namespace std;

using vi = vector<int>;

void solution() {
    long long ans = 0;
    int N;
    cin >> N;
    vector<int> nums(N);
    int sum = 0;
    for (int i = 0; i < N; ++i) {
        cin >> nums[i];
        sum += abs(nums[i]);
    }

    vector<int> cnt(2 * sum + 1);
    cnt[sum] = 1;
    int prefix = 0;
    for (int i = 0; i < N; ++i) {
        prefix += nums[i];
        for (int j=0; j * j <= sum + prefix; ++j) {
            ans += cnt[sum + prefix - j * j];
        }
        cnt[sum + prefix]++;
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