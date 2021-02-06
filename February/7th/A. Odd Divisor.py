if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                break
        if n == 1:
            print("NO")
        else:
            print("YES")