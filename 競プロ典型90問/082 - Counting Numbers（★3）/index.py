L, R = map(int, input().split())

NUM = 1000000007

left = L
right = R

ans = 0
for n in range(1, 20):
    temp = 10**n - 1
    if left <= temp:
        if right <= temp:
            ans += ((right + left) * (right - left + 1) // 2) * n % NUM
            break
        else:
            ans += ((temp + left) * (temp - left + 1) // 2) * n % NUM
            left = temp + 1
            continue

print(ans % NUM)
