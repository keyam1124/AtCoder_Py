S = input()
ans = S
while True:
    if len(ans) == 6:
        print(ans)
        exit()
    ans += S
