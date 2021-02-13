from collections import defaultdict
from math import ceil

def solution():
    N, X = map(int, input().split())
    nums = list(map(int, input().split()))

    idx = 1
    d = defaultdict(list)
    for num in nums:
        num = ceil(num / X)
        d[num].append(idx)
        idx += 1

    ans = []
    for k in sorted(d.keys()):
        ans += d[k]
    
    return ' '.join([str(idx) for idx in ans])


if __name__ == '__main__':
    T = int(input())
    for testCase in range(1, T+1):
        ans = solution()
        print("Case #{}: {}".format(testCase, ans))