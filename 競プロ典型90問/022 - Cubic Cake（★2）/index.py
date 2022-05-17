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


A, B, C = map(int, input().split())
gcd_ab = gcd(A, B)
gcd_abc = gcd(gcd_ab, C)

ans = A // gcd_abc + B // gcd_abc + C // gcd_abc - 3
print(ans)
