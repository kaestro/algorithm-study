
# def unusual_matrix(mat1, mat2, n):
#     set1 = set()
#     set2 = set()
#     set3 = set()
#     set4 = set()

#     for i in range(n):
#         set1.add(tuple(mat1[i]))
#         set1.add(tuple([0 if num == 1 else 1 for num in mat1[i]]))
#         set2.add(tuple(mat2[i]))
#         set2.add(tuple([0 if num == 1 else 1 for num in mat2[i]]))
    
#     for j in range(n):
#         temp1 = []
#         temp2 = []
#         for i in range(n):
#             temp1.append(mat1[i][j])
#             temp2.append(mat2[i][j])
        
#         set3.add(tuple(temp1))
#         set3.add(tuple([0 if num == 1 else 1 for num in temp1]))
#         set4.add(tuple(temp2))
#         set4.add(tuple([0 if num == 1 else 1 for num in temp2]))

    
#     return len(set1) == len(set2) and len(set3) == len(set4)

# N = int(input())


# for _ in range(N):
#     n = int(input())
#     mat1 = []
#     mat2 = []
#     for _ in range(n):
#         row = [int(c) for c in input()]
#         mat1.append(row)
    
#     empty = input()
#     for _ in range(n):
#         row = [int(c) for c in input()]
#         mat2.append(row)

#     if unusual_matrix(mat1,mat2,n):
#         print("YES")
#     else:
#         print("NO")
        
import copy
from fractions import Fraction
 
def gauss(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = len(a)
    p = len(b[0])
    det = 1
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det
 
        for j in range(i + 1, n):
            t = a[j][i]/a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t*a[i][k]
            for k in range(p):
                b[j][k] -= t*b[i][k]
 
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t*b[j][k]
        t = 1/a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t
    return det, b
 
def zeromat(p, q):
    return [[0]*q for i in range(p)]
 
def matmul(a, b):
    n, p = len(a), len(a[0])
    p1, q = len(b), len(b[0])
    if p != p1:
        raise ValueError("Incompatible dimensions")
    c = zeromat(n, q)
    for i in range(n):
        for j in range(q):
                c[i][j] = sum(a[i][k]*b[k][j] for k in range(p))
    return c
 
 
def mapmat(f, a):
    return [list(map(f, v)) for v in a]
 
def ratmat(a):
    return mapmat(Fraction, a)