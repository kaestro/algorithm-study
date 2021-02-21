def maximum_coins(mat):
    n = len(mat)
    max_coins = 0

    def sum_diagonal(i,j):
        s = 0
        while i < n and j < n:
            s += mat[i][j]
            i += 1
            j += 1
        # print(s)
        return s

    for i in range(n):
        max_coins = max(max_coins, sum_diagonal(i,0))
        max_coins = max(max_coins, sum_diagonal(0,i))

    return max_coins  

mat = [
    [0,0,0,0,0],
    [1,1,1,1,0],
    [2,2,2,8,0], 
    [1,1,1,0,0], 
    [0,0,0,0,0]]

print(maximum_coins(mat))


# N = int(input())
# for i in range(N):
#     mat = []
#     for j in range(int(input())):
#         row = [int(x) for x in input().split()]
#         mat.append(row)
#     print("Case #{}: {}".format(i+1,maximum_coins(mat)))