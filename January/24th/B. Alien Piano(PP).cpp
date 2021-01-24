#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;
using ll = long long;
const int MAX_N = 1e4;
int dp[4][MAX_N], N, A[MAX_N];
int chk(int& r1, int& r2, int& p){
	if(A[p - 1] < A[p]) return !(r1 < r2);
	return A[p - 1] == A[p] ? !(r1 == r2) : !(r1 > r2);
}
int rec(int r, int p){
	if(p == N) return 0;
	int& ret = dp[r][p];
	if(ret != -1) return ret;
	ret = 1e9;
	for(int i=0;i<4;i++)
		ret = min(ret, rec(i, p+1) + chk(r, i, p));
	return ret;
}
int main() {
	int T, tc, i, ans;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d", &N);
		for(i=0;i<N;i++) scanf("%d", &A[i]);

		memset(dp, -1, sizeof dp);
		ans = N;
		for(i=0;i<4;i++)
			ans = min(ans, rec(i, 1));
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}