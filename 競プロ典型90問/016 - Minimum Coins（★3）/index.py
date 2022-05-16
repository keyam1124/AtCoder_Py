N = int(input())
A, B, C = map(int, input().split())

max = 9999

ans = 10000
for a_cnt in range(0, max + 1):
    a_yen = A * a_cnt
    for b_cnt in range(0, max + 1 - a_cnt):
        b_yen = B * b_cnt
        if N < a_yen + b_yen:
            continue
        c_yen = N - a_yen - b_yen
        if c_yen % C == 0:
            c_cnt = c_yen // C
            temp = a_cnt + b_cnt + c_cnt
            if ans > temp:
                ans = temp

print(ans)
