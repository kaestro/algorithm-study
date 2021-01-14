#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int res = 0;
        sort(people.begin(), people.end());
        for (auto it = people.begin(); it != people.end(); ++it) {
            auto weight = *it;
            auto lb = upper_bound(it, people.end(), limit - weight);
            lb--;
            if (lb > it) {
                people.erase(lb);
            }
            res += 1;
        }
        return res;
    }
};

int main() {
    vector<int> people = {3,2,2,1};
    int limit = 3;
    Solution sol;
    sol.numRescueBoats(people, limit);
    return 0;
}