N = int(input())

already = dict()
for i in range(1, N + 1):
    S = input()
    if already.get(S) is None:
        print(i)
        already[S] = 0
