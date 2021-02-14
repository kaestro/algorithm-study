#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;
using ll = long long;
const int MAX_N = 1e5;
int main() {
	int T, tc, N, X, i, A[MAX_N];
	priority_queue<pair<int, int>> pq;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d%d", &N, &X);
		for (i = 0; i < N; i++) {
			scanf("%d", &A[i]);
			A[i] = A[i] / X + (A[i] % X > 0);
			pq.push({ -A[i], -i });
		}
		printf("Case #%d: ", tc);
		while (!pq.empty()) {
			printf("%d ", -pq.top().second + 1);
			pq.pop();
		}
		puts("");
	}
	return 0;
}