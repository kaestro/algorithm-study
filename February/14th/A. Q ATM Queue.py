import queue

def solution():
    N, X = map(int, input().split())
    nums = list(map(int, input().split()))

    idx = 1
    q = queue.Queue()
    for num in nums:
        q.put((idx, num))
        idx += 1
    
    ans = []
    while q.qsize() > 0:
        idx, amount = q.get()
        amount -= X
        if amount > 0:
            q.put((idx, amount))
        else:
            ans.append(idx)

    return ' '.join([str(idx) for idx in ans])


if __name__ == '__main__':
    T = int(input())

    for testCase in range(1, T+1):
        ans = solution()
        print("Case #{}: {}".format(testCase, ans))
    