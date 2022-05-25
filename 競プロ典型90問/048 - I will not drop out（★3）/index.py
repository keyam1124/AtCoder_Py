N, K = map(int, input().split())
A_subtract_B = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A_subtract_B.append(a - b)
    B.append(b)

c = A_subtract_B + B
c.sort(reverse=True)
print(sum(c[:K]))
