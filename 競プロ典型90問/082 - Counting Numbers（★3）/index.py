L, R = map(int, input().split())
left = L
right = R
NUM = 1000000007
ans = 0
for i in range(1, 20):
    temp = 10**i - 1
    if temp >= left:
        if temp >= right:
            ans += ((right + left) * (right - left + 1) // 2) * i % NUM
            break
        else:
            ans += ((left + temp) * (temp - left + 1) // 2) * i % NUM
            left = temp + 1

print(ans % NUM)
