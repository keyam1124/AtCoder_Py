def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())
cnt = len(prime_factorize(n))
if cnt == 1:
    print(0)
else:
    ans = 1
    while 2**ans < cnt:
        ans += 1

    print(ans)
