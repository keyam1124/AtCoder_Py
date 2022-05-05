def from10(val: int, base: int):
    syou = val
    res = ""
    while syou > 0:
        mod = syou % base
        res = str(mod) + res
        syou //= base
    return res


def to10(val: int, base: int):
    res = 0
    for i in range(len(str(val))):
        res += (val % 10) * (base**i)
        val //= 10
    return res


n, k = map(int, input().split())
if n == 0:
    print(0)
else:
    for i in range(k):
        n10 = to10(n, 8)
        n = from10(n10, 9)
        n = int(str(n).replace("8", "5"))

    print(n)
