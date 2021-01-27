from collections import deque

class Solution:
    answer = 1e6
    def isPassable(self, heights:list, k:int) -> bool:
        R, C = len(heights), len(heights[0])
        check = [[False for i in range(C)] for j in range(R)]
        check[0][0] = True
        q = deque()
        q.append((0,0)) # row, col

        dRow = [1,-1,0,0]
        dCol = [0,0,1,-1]

        while len(q) > 0:
            temp = q.popleft()
            r, c = temp[0], temp[1]
            if r == R-1 and c == C-1:
                return True
            for d in range(4):
                newR = r + dRow[d]
                newC = c + dCol[d]
                if newR < 0 or newC < 0 or newR >= R or newC >= C:
                    continue
                if check[newR][newC] or abs(heights[newR][newC]-heights[r][c]) > k:
                    continue
                check[newR][newC] = True
                q.append((newR, newC))
        return False

    def binarySearch(self, heights:list, L:int, R:int):
        mid = (L + R) // 2
        if self.isPassable(heights, mid):
            self.answer = min(self.answer, mid)
            if L < R:
                self.binarySearch(heights, L, mid)
        else:
            self.binarySearch(heights, mid+1, R)

    def minimumEffortPath(self, heights:list) -> int:
        L, R = 0, 1e6+1
        self.binarySearch(heights, L, R)
        return int(self.answer)
