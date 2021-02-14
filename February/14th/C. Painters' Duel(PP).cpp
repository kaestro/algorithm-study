#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;
using ll = long long;
const int MAX_N = 20;
int used[MAX_N][MAX_N];
int S, C, dy[2][3] = { {-1, -1, 1}, {-1,1,1} }, dx[2][3] = { {-1, 1, 1}, {-1, -1, 1} };
int gy(int y, int x) { return (y - 1) * 2 - !(x % 2); }
int back(int ay, int ax, int by, int bx, int st) {
	if (st == 2) return 0;
	int stuck = 0, i, d, ret = -1e9;

	d = ax % 2;
	for (i = 0; i < 3; i++) {
		int ty = ay + dy[d][i], tx = ax + dx[d][i];
		if (0 <= ty && 0 <= tx && tx <= ty && ty < 2 * S - 1) {
			if (used[ty][tx]) stuck++;
			else {
				used[ty][tx] = 1;
				if(st)
					ret = max(ret, 1 + back(ty, tx, by, bx, st));
				else ret = max(ret, 1 - back(by, bx, ty, tx, st));
				used[ty][tx] = 0;
			}
		}
		else stuck++;
	}
	if (stuck == 3)
		return -back(by, bx, ay, ax, st + 1);
	return ret;
}
int main() {
	int T, tc, RA, PA, RB, PB, i, y, x;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		memset(used, 0, sizeof used);
		scanf("%d%d%d%d%d%d", &S, &RA, &PA, &RB, &PB, &C);
		RA = gy(RA, PA); PA--;
		RB = gy(RB, PB); PB--;
		for(i=0;i<C;i++) {
			scanf("%d%d", &y, &x);
			y = gy(y, x); x--;
			used[y][x] = 1;
		}
		used[RA][PA] = used[RB][PB] = 1;
		printf("Case #%d: %d\n", tc, back(RA, PA, RB, PB, 0));
	}
	return 0;
}