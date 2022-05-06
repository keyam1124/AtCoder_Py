n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)

a += a
right = 0
temp_sum = 0

for left in range(n):
    while 10 * temp_sum < sum_a:
        temp_sum += a[right]
        right += 1
    if 10 * temp_sum == sum_a:
        print("Yes")
        break
    temp_sum -= a[left]
else:
    print("No")
