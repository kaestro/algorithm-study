#include <bits/stdc++.h>
using namespace std;
using ll = long long;

void solve(int trial) {
    int n;
    cin >> n;
    vector<ll> e(n), r(n), s(n);
    ll sum = 0;
    for (int i = 0; i < n; ++i) {
        cin >> e[i] >> r[i];
        s[i] = e[i] + r[i];
        sum += e[i];
    }
    priority_queue<pair<ll, ll>> toylist;
    ll cur_time = sum, max_time = sum;
    int removed = 0, count = 0;
    for (int i = 0; i < n; ++i) {
        toylist.push(make_pair(s[i], i));
        cur_time += e[i];

        while (!toylist.empty()) {
            auto temp = toylist.top();
            if (sum >= temp.first) {
                break;
            } else {
                int ind = temp.second;
                cur_time -= e[ind] * 2;
                sum -= e[ind];
                count += 1;
                toylist.pop();
            }
        }
        if (cur_time > max_time) {
            removed = count;
            max_time = cur_time;
        } else if (cur_time == max_time) {
            removed = min(removed, count);
        }
    }

    if (toylist.empty()) {
        cout << "Case #" << trial <<": ";
        cout << removed << " " << max_time << endl;
    } else {
        cout << "Case #";
        cout << count << " INDEFINITELY" << endl;
    }
}