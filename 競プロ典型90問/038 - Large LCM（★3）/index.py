def gcd(a: int, b: int) -> int:
    if a < b:
        temp = a
        a = b
        b = temp

    while b != 0:
        m = a % b
        a = b
        b = m

    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


MAX = 1000000000000000000
A, B = map(int, input().split())
ans = lcm(A, B)
if ans > MAX:
    print("Large")
    exit()
print(ans)
