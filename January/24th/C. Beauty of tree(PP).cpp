#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;
using ll = long long;
const int MAX_N = 5e5, MAX_D = 20;
vector<int> adj[MAX_N];
int A, B, p[MAX_N][MAX_D];
ll ca[MAX_N], cb[MAX_N];
int getNthParent(int u, int nth) {
	for (int i = 0; u != -1 && i < MAX_D; i++) if (nth & (1 << i))
		u = p[u][i];
	return u;
}
void dfs(int u) {
	for (int& v : adj[u])
		dfs(v);
	ca[u]++, cb[u]++;
	int pa = getNthParent(u, A), pb = getNthParent(u, B);
	if (pa != -1) ca[pa] += ca[u];
	if (pb != -1) cb[pb] += cb[u];
}
int main() {
	int T, tc, N, i, d;
	double ans, pa, pb;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d%d%d", &N, &A, &B);
		memset(p, -1, sizeof p);
		for (i = 0; i < N; i++) {
			adj[i].clear();
			ca[i] = cb[i] = 0;
		}
		for (i = 1; i < N; i++) {
			scanf("%d", &p[i][0]);
			p[i][0]--;
			adj[p[i][0]].push_back(i);
		}
		for (d = 1; d < MAX_D; d++)
			for (i = 1; i < N; i++) if(p[i][d - 1] != -1)
				p[i][d] = p[p[i][d - 1]][d - 1];

		dfs(0);
		ans = 0;
		for (i = 0; i < N; i++) {
			pa = (double)ca[i] / N;
			pb = (double)cb[i] / N;
			ans += pa * (1 - pb) + pb * (1 - pa) + pa * pb;
		}
		printf("Case #%d: %.11lf\n", tc, ans);
	}
	return 0;
}