from collections import Counter
from math import factorial

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort(reverse=True)

        last_begin = a.index(a[k-1])
        a_cnt = Counter(a)[a[k-1]]

        a_used_cnt = k-1 - last_begin + 1
        ans = factorial(a_cnt)
        ans //= factorial(a_cnt - a_used_cnt)
        ans //= factorial(a_used_cnt)
        print(ans % (10 ** 9 + 7))