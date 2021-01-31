if __name__ == "__main__":
    T = int(input())
    for testCase in range(1, T+1):
        N, Q = map(int, input().split())
        doors = list(map(int, input().split()))
        ans = []

        for i in range(Q):
            S, K = map(int, input().split())
            K -= 1
            S -= 1
            left, right = S - 1, S

            while K > 0:
                if left < 0:
                    S = right+1
                    right += 1
                elif right >= N-1:
                    S = left
                    left -= 1
                else:
                    if doors[left] < doors[right]:
                        S = left
                        left -= 1
                    else:
                        S = right+1
                        right += 1
                K -= 1
            ans.append(S+1)

        print("Case #{}: {}".format(testCase, ' '.join([str(num) for num in ans])))