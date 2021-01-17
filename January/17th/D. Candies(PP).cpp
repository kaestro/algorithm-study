#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<unordered_map>
#include<set>
#include<queue>
using namespace std;
using ll = long long;
const int MAX_N = 26;
int main() {
	char b[30][31], ans[27];
	int T, tc, i, j, k, R, C, dy[] = { 0,0,1,-1 }, dx[] = { 1,-1,0,0 }, ind[26], cnt, tot, valid[26];
	bool vi[30][30];
	set<int> adj[MAX_N];
	queue<pair<int, int>> q;
	queue<int> toq;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d%d\n", &R, &C);
		for (i = 0; i < 26; i++) {
			adj[i].clear();
			valid[i] = ind[i] = 0;
		}
		cnt = tot = 0;
		memset(vi, 0, sizeof vi);

		for (i = 0; i < R; i++) scanf("%s", b[i]);
		for (i = 0; i < R; i++)
			for (j = 0; j < C; j++) if (!vi[i][j]) {
				valid[b[i][j] - 'A'] = 1;
				vi[i][j] = 1;
				q.push({ i, j });
				while (!q.empty()) {
					auto u = q.front(); q.pop();
					for (k = 0; k < 4; k++) {
						int ty = u.first + dy[k], tx = u.second + dx[k];
						if (0 <= ty && ty < R && 0 <= tx && tx < C) {
							if (b[u.first][u.second] != b[ty][tx]) {
								if (k == 3) adj[b[u.first][u.second] - 'A'].insert(b[ty][tx] - 'A');
							}
							else if (!vi[ty][tx]) {
								vi[ty][tx] = 1;
								q.push({ ty, tx });
							}
						}
					}
				}
			}
		for (i = 0; i < 26; i++) {
			tot += valid[i];
			for (const int& v : adj[i]) ind[v]++;
		}
		for (i = 0; i < 26; i++) if (!ind[i] && valid[i])
			toq.push(i);
		while (!toq.empty()) {
			int u = toq.front(); toq.pop();
			ans[cnt++] = u + 'A';
			for (const int& v : adj[u]) {
				ind[v]--;
				if (!ind[v]) toq.push(v);
			}
		}
		ans[cnt] = 0;
		if (cnt == tot) printf("Case #%d: %s\n", tc, ans);
		else printf("Case #%d: -1\n", tc);
	}
	return 0;
}