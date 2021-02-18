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
	char S[MAX_N + 1];
	const char* kick = "KICK", * st = "START";
	int T, tc, s, ans, i, j;
	scanf("%d\n", &T);
	for (tc = 1; tc <= T; tc++) {
		scanf("%s", S);
		for (ans = s = i = 0; S[i]; i++) {
			if (S[i] == 'K') {
				for (j = 0; j < 4; j++) {
					if (S[i + j] != kick[j]) break;
					if (j == 3)
						s++;
				}
			}
			else {
				for (j = 0; j < 5; j++) {
					if (S[i + j] != st[j]) break;
					if (j == 4)
						ans += s;
				}
			}
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}