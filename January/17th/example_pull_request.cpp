// https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3599/
// binary search를 이용해서문제를해결하려했는데 잘 안되네요.

#include <bits/stdc++.h>

using namespace std;

const int MOD = 1e9 + 7;

class Solution {
public:
    int createSortedArray(vector<int>& instructions) {
        int ans = 0;
        for (auto it = instructions.begin(); it != instructions.end(); ++it) {
            sort(instructions.begin(), it);
            auto ub = upper_bound(instructions.begin(), it, *it);
            auto lb = lower_bound(instructions.begin(), it, *it);
            int left = lb - instructions.begin();
            int right = it - ub;
            ans += min(left, right);
            ans %= MOD;
        }
        return ans;
    }
};

