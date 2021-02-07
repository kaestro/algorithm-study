from collections import defaultdict
def ball_in_berland(lst1, lst2, k):
    d1 = defaultdict(list)
    d2 = defaultdict(list)

    for i in range(k):
        d1[lst1[i]].append(lst2[i])
        d2[lst2[i]].append(lst1[i])
    
    result = 0
    for key, value in d1.items():
        for n in value:
            temp = k + 1
            temp -= len(value)
            temp -= len(d2[n])
            result += temp

    return result // 2

lst1 = [1]
lst2 = [1]
k = 1

print(ball_in_berland(lst1,lst2,k))