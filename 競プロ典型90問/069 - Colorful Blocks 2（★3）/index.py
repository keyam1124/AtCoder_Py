num = 1000000007
N, K = map(int, input().split())

if N == 1:
    print(K % num)
elif N == 2:
    print(K * (K - 1) % num)
else:
    print((K * (K - 1) % num) * pow((K - 2), (N - 2), num) % num)
