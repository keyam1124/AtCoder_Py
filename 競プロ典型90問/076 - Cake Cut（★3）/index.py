N = int(input())
A = list(map(int, input().split()))
sum_a = sum(A)

A += A
right = 0

temp_sum = 0

for left in range(N):
    while 10 * temp_sum < sum_a:
        temp_sum += A[right]
        right += 1
    if 10 * temp_sum == sum_a:
        print("Yes")
        exit()
    temp_sum -= A[left]
print("No")
