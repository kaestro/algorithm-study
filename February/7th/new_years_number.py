def new_years_number(n):
    
    div = n // 2020
 

    return n % 2021 == 0 or n % 2020 == 0 or n >= 2020*div and n <= 2021*div
    # table = [False for _ in range(n+1)]
    # table[0] = True
    # for i in range(1,n+1):
    #     if i < 2020:
    #         table[i] = False
    #     elif i == 2020 or i == 2021:
    #         table[i] = True
    #     else:
    #         table[i] = table[i-2020] or table[i-2021]

    # return table[-1]

print(new_years_number(8085))