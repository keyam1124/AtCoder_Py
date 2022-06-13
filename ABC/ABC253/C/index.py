import heapq

Q = int(input())
S = dict()

mx = []
mn = []

s_max = 0
s_min = 10000000000
for i in range(Q):
    query = input().split()
    q_type = query[0]
    if q_type == "1":
        x = int(query[1])

        heapq.heappush(mx, -x)
        heapq.heappush(mn, x)

        if S.get(x) is None:
            S[x] = 1
        else:
            S[x] += 1
    elif q_type == "2":
        x = int(query[1])

        if S.get(x) is None:
            continue
        x_cnt = S[x]
        c = int(query[2])
        del_cnt = min(c, x_cnt)
        S[x] -= del_cnt

    else:
        while S[-mx[0]] == 0:  # q_type=2で削除された要素は除いて最大値
            heapq.heappop(mx)
        while S[mn[0]] == 0:  # q_type=2で削除された要素は除いて最小値
            heapq.heappop(mn)
        print(-mx[0] - mn[0])
