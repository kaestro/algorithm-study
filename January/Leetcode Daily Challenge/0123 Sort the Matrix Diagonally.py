class Solution:
    def diagonalSort(self, mat:list) -> list:
        R, C = len(mat), len(mat[0])

        for row in range(R):
            r, c = row, 0
            temp = []
            while r < R and c < C:
                temp.append(mat[r][c])
                r += 1
                c += 1
            temp.sort()
            r, c = row, 0
            for i in range(len(temp)):
                mat[r+i][c+i] = temp[i]
        
        for col in range(1, C):
            r, c = 0, col
            temp = []
            while r < R and c < C:
                temp.append(mat[r][c])
                r += 1
                c += 1
            temp.sort()
            r, c = 0, col
            for i in range(len(temp)):
                mat[r+i][c+i] = temp[i]
        return mat