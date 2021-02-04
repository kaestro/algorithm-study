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
    int t, c;
    ll n;
    scanf("%d", &t);
    while (t--) {
        scanf("%lld", &n);
        while (n % 2 == 0)
            n /= 2;
        puts(n > 1 ? "YES" : "NO");
    }
    return 0;
}