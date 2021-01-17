import sys

T = int(sys.stdin.readline())
for t in range(1, T+1):
    R, C = map(int, sys.stdin.readline().split())
    S = [list(sys.stdin.readline().rstrip()) for i in range(R)]

    graph = [[False for i in range(26)] for j in range(26)]
    failFlag = False
    for c in range(C):
        for r in range(R-1, -1, -1):
            fr = ord(S[r][c]) - ord('A')
            for r2 in range(r - 1, -1, -1):
                to = ord(S[r2][c]) - ord('A')
                if fr == to:
                    continue
                graph[fr][to] = True
                if graph[to][fr]:
                    failFlag = True
    
    if failFlag:
        print("Case #" + str(t) + ": -1")
    else:
        P = []
        temp = dict()
        for r in range(R):
            for c in range(C):
                if not temp.__contains__(S[r][c]):
                    temp.update({S[r][c]:0})
        pList = list(temp.keys())
        for p in pList:
            cnt = 0
            for i in range(26):
                if graph[i][ord(p) - ord('A')]:
                    cnt += 1
            P.append([p, cnt])
        
        answer = []
        check = [False for i in range(26)]

        for i in range(len(P)):
            P.sort(key=lambda x: x[1])
            idx = 0
            while idx < len(P):
                if check[ord(P[idx][0]) - ord('A')]:
                    idx += 1
                    continue
                check[ord(P[idx][0]) - ord('A')] = True
                answer.append(P[idx][0])
                break

            for j in range(26):
                if graph[ord(P[idx][0]) - ord('A')][j]:
                    for k in range(len(P)):
                        if P[k][0] == (chr(j + ord('A'))):
                            P[k][1] -= 1
                            break

        print("Case #" + str(t) + ": ", end ='')
        for i in range(len(answer)):
            print(answer[i], end ='')
        print('')                      
