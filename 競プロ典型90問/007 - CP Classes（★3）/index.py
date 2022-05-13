import bisect

N = int(input())
A = list(map(int, input().split(" ")))
A.sort()
Q = int(input())

MAX = 10000000000
for _ in range(Q):
    B = int(input())

    # 二分探索
    idx = bisect.bisect_left(A, B)
    abs1 = MAX if idx == 0 else abs(B - A[idx - 1])
    abs2 = MAX if idx == len(A) else abs(B - A[idx])
    if abs1 > abs2:
        print(abs2)
    else:
        print(abs1)
