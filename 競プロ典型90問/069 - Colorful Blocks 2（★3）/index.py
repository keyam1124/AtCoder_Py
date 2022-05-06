num = 1000000007
n, k = map(int, input().split())

if n == 1:
    print(k)
    exit()

if n == 2 and k < 2:
    print(0)
    exit()

if n > 2 and k <= 2:
    print(0)
    exit()

mod = k % num
mod *= (k - 1) % num
mod *= pow(k - 2, n - 2, num)
print(mod % num)
