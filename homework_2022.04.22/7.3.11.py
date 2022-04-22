n = int(input())
j = int(input())

a = [[int(x) for x in input().split(' ')] for _ in range(n)]

res = int(1e10)

for i in range(n):
    for k in range(n):
        if i == k or i == j or k == j:
            continue
        cur = a[i][j] + a[j][k] - a[i][k]
        if cur < res:
            res = cur
print(res // 2)