#include<cstdio>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;
using ll = long long;
const int MAX_N = 15, LIMIT = 1e7 + 1;
int main() {
    vector<int> p;
    int t, n, a, b;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        //2020a + 2021b = n
        //(a + b) 2020 + b = n
        b = n % 2020;
        puts((n - b)/2020 - b >= 0 ? "YES" : "NO");
    }
    return 0;
}