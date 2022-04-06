# https://github.com/PennyroyalTea/bioinformatics-homeworks/blob/master/homework_2022.03.18/5.10.3.py

match, mismatch, indel = map(int, input().split(' '))
s = input()
t = input()

dp = [[int(-1e9)] * (len(t) + 1) for _ in range(len(s) + 1)]
cnt = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

dp[0][0] = 0
cnt[0][0] = 1

for i in range(len(s) + 1):
    for j in range(len(t) + 1):
        if i >= 1 and j >= 1:
            if s[i - 1] == t[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + match)
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] - mismatch)
        if i >= 1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] - indel)
        if j >= 1:
            dp[i][j] = max(dp[i][j], dp[i][j - 1] - indel)
        # cnt update
        if i >= 1 and dp[i][j] == dp[i - 1][j] - indel:
            cnt[i][j] += cnt[i - 1][j]
        if j >= 1 and dp[i][j] == dp[i][j - 1] - indel:
            cnt[i][j] += cnt[i][j - 1]
        if i >= 1 and j >= 1:
            if s[i - 1] == t[j - 1] and dp[i][j] == dp[i - 1][j - 1] + match:
                cnt[i][j] += cnt[i - 1][j - 1]
            elif s[i - 1] != t[j - 1] and dp[i][j] == dp[i - 1][j - 1] - mismatch:
                cnt[i][j] += cnt[i - 1][j - 1]

x, y = len(s), len(t)

res1, res2 = '', ''
while x > 0 or y > 0:
    if x >= 1 and y >= 1 and (s[x - 1] == t[y - 1] or dp[x - 1][y - 1] - mismatch == dp[x][y]):
        res1 += s[x - 1]
        res2 += t[y - 1]
        x, y = x - 1, y - 1
    elif x >= 1 and dp[x - 1][y] - indel == dp[x][y]:
        res1 += s[x - 1]
        res2 += '-'
        x -= 1
    else:
        res1 += '-'
        res2 += t[y - 1]
        y -= 1

print(cnt[-1][-1])