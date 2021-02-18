#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<cmath>
using namespace std;
using ll = long long;
const int MAX_N = 5e3 + 5;
int main() {
	int T, tc, A, N, i, j, t, s;
	double coe[2][MAX_N] = {}, ans;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d", &N);
		t = 0;
		coe[t][1] = coe[t][2] = 1;
		for (i = 3; i <= N; i++, t = !t) {
			memset(coe[!t], 0, sizeof coe[!t]);
			s = 0;
			for (j = 1; j <= i; j++, s++)
				coe[!t][j] = ((j == 1 || j == i ? 1 : 2) + s * coe[t][j - 1] + (i - 1 - s) * coe[t][j]) / (i - 1.);
		}

		ans = 0;
		for (i = 1; i <= N; i++) {
			scanf("%d", &A);
			ans += A * coe[t][i];
		}
		printf("Case #%d: %.11lf\n", tc, ans);
	}
	return 0;
}