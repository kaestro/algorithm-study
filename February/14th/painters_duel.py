def painters_duel (s, r_a,p_a,r_b,p_b,c):
    # print(c)

    board = {}
    for i in range(1,s+1):
        board[i] = {i:0 for i in range(1,i*2)}

    board[r_a][p_a] = 1
    board[r_b][p_b] = -1



    def neighbors(i,j):
        n = []
        if j != 1:
            n.append((i,j-1))
        if j != i*2-1:
            n.append((i,j+1))
        if j % 2 == 0:
            n.append((i-1,j-1))
        else:
            if i != s:
                n.append((i+1,j+1))

        result = []
        for node in n:
            if board[node[0]][node[1]] == 0 and node not in c:
                result.append(node)

        return result

        

            


    def evaluate(board):
        s = 0
        for value in board.values():
            s += sum(value.values())
        return s



    #i1,j1 position of alma
    #i2,j2 position of berthe
    def minimax(i1,j1,i2,j2,maximizingPlayer,board):
        # print(board)
        n1 = neighbors(i1,j1)
        n2 = neighbors(i2,j2)
        # if maximizingPlayer:
        #     neighbors(i1,j1,n)
        # else:
        #     neighbors(i2,j2,n)
        if not n1 and not n2:
            return evaluate(board)
        
        if maximizingPlayer:
            value = float('-inf')
            if n1:
                for node in n1:
                    # print(node)
                    (i,j) = node
                    board[i][j] = 1
                    value = max(value, minimax(i,j,i2,j2,False,board))
                    board[i][j] = 0
            else:
                value = max(value, minimax(i1,j1,i2,j2,False,board) )

            return value
        else:
            value = float('inf')
            if n2:
                for node in n2:
                    (i,j) = node
                    board[i][j] = -1
                    value = min(value, minimax(i1,j1,i,j,True,board))
                    board[i][j] = 0
            else:
                value = min(value, minimax(i1,j1,i2,j2,True,board) )
            return value

    return minimax(r_a,p_a,r_b,p_b,True,board)

# s = set()
# s.add((2,1))
# s.add((3,1))
# print(painters_duel(3,3,2,2,3,s))
N = int(input())


for i in range(N):
    input1 = [int(x) for x in input().split()]
    c = set()
    for j in range(input1[-1]):
        lst = [int(y) for y in input().split()]
        c.add(tuple(lst))
    
    print("Case #{}: {}".format(i+1,painters_duel(*input1[:-1],c)))