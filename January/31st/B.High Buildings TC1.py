def backTrack(res:list, nums: list, N, step):
    if step == 0:
        res.append(nums)
        return
    
    step -= 1
    for i in range(1, N+1):
        backTrack(res, nums+[i], N, step)

if __name__ == "__main__":
    T = int(input())
    for testCase in range(1, T+1):
        N, A, B, C = map(int, input().split())
        cities = []
        backTrack(cities, [], N, N)
        res = []
        for buildings in cities:

            isImpossible = False

            maxheight = max(buildings)
            if buildings.count(maxheight) != C:
                continue

            rightCnt = 0
            for i in range(N):
                curHeight = buildings[i]
                
                for j in range(i, N):
                    if buildings[j] > curHeight:
                        break
                    elif j == N-1:
                        rightCnt += 1
            
            if rightCnt != B:
                continue

            leftCnt = 0
            for i in range(N-1, -1, -1):
                curHeight = buildings[i]
                for j in range(i, -1, -1):
                    if buildings[j] > curHeight:
                        break
                    elif j == 0:
                        leftCnt += 1
            
            if leftCnt == A:
                res = buildings
                break


        if res == []:
            print("Case #{}: IMPOSSIBLE".format(testCase))
        else:
            print("Case #{}: {}".format(testCase, ' '.join([str(num) for num in res])))