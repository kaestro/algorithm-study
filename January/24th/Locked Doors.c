#include <stdio.h>
#define MAX 100001

int T, N, Q;
int D[MAX], S[MAX], K[MAX];

int main(){
	int L, R, last;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		// input
		scanf("%d %d", &N, &Q);
		for (int i = 1; i < N; i++)
			scanf("%d", &D[i]);
		for (int i = 0; i < Q; i++)
			scanf("%d %d", &S[i], &K[i]);

		printf("Case #%d: ", t);
		for (int q = 0; q < Q; q++){
			L = S[q], R = S[q];
			last = S[q];
			while (K[q] > 1){
				if (L == 1){
					R++;
					K[q]--;
					last = R;
				}
				else if (R == N){
					L--;
					K[q]--;
					last = L;
				}
				else{
					if (D[L-1] < D[R]){
						L--;
						K[q]--;
						last = L;
					}
					else{
						R++;
						K[q]--;
						last = R;
					}
				}
			}
			printf("%d ", last);
		}
		printf("\n");
	}
	return 0;
}
