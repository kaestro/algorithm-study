if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        num = int(input())
        ans = "NO"
        for _ in range(2020):
            if num % 2020 == 0:
                ans = "YES"
                break

            num -= 2021
            if num < 0:
                break
        print(ans)