
def unusual_matrix(mat1, mat2, n):
    set1 = set()
    set2 = set()
    set3 = set()
    set4 = set()

    for i in range(n):
        set1.add(tuple(mat1[i]))
        set1.add(tuple([0 if num == 1 else 1 for num in mat1[i]]))
        set2.add(tuple(mat2[i]))
        set2.add(tuple([0 if num == 1 else 1 for num in mat2[i]]))
    
    for j in range(n):
        temp1 = []
        temp2 = []
        for i in range(n):
            temp1.append(mat1[i][j])
            temp2.append(mat2[i][j])
        
        set3.add(tuple(temp1))
        set3.add(tuple([0 if num == 1 else 1 for num in temp1]))
        set4.add(tuple(temp2))
        set4.add(tuple([0 if num == 1 else 1 for num in temp2]))

    
    return len(set1) == len(set2) and len(set3) == len(set4)

N = int(input())


for _ in range(N):
    n = int(input())
    mat1 = []
    mat2 = []
    for _ in range(n):
        row = [int(c) for c in input()]
        mat1.append(row)
    
    empty = input()
    for _ in range(n):
        row = [int(c) for c in input()]
        mat2.append(row)

    if unusual_matrix(mat1,mat2,n):
        print("YES")
    else:
        print("NO")
        