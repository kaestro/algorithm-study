#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
using namespace std;
using ll = long long;
const int MAX_N = 100;
int main() {
	int T, tc, N, i, A, B, C, R, ans[MAX_N] = {}, s, d;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%d%d%d%d", &N, &A, &B, &C);
		R = N - (A + B - C);
		printf("Case #%d: ", tc);
		if (R >= 0 && !(A == 1 && B == 1 && C == 1 && N != 1)) {
			if (C == 1) {
				A > B ? B -= C : A -= C;
				C--;
				for (i = 0; i < A; i++) ans[i] = i + 1;
				for (i = 0; i < B; i++) ans[N - 1 - i] = i + 1;

				d = A > B ? 1 : -1;
				i = (A > B ? A - 2 : N - B + 1);
				ans[i] = N - 1;
				i += d;
				while (R--) {
					ans[i] = 1;
					i += d;
				}
				ans[i] = N;
			}
			else {
				A -= C - 1, B -= C - 1;
				C -= 2;
				for (i = 0; i < A; i++) ans[i] = i + 1;
				for (i = 0; i < B; i++) ans[N - 1 - i] = i + 1;
				ans[A - 1] = ans[N - B] = N;
				i = A;
				while (R--) ans[i++] = 1;
				while (C--) ans[i++] = N;
			}
			for (i = 0; i < N; i++)
				printf("%d ", ans[i]);
		}
		else printf("IMPOSSIBLE");
		puts("");
	}
	return 0;
}