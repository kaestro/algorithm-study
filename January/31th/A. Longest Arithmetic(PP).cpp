#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;
using ll = long long;
const int MAX_N = 2e5;
int main() {
	int T, tc, i, N, diff, bef, A, ans, tmp;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d", &N);
		tmp = ans = 2;
		scanf("%d%d", &bef, &A);
		diff = A - bef;
		bef = A;
		for (i = 2; i < N; i++) {
			scanf("%d", &A);
			if (A - bef == diff) tmp++;
			else {
				tmp = 2;
				diff = A - bef;
			}
			bef = A;
			ans = max(ans, tmp);
		}

		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}