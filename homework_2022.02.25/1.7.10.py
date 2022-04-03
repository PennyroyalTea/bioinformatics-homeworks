from itertools import accumulate
s = input()

g = map(lambda c: int(c == 'G'), s)
g_pref = list(accumulate(list(g)))
c = map(lambda c: int(c == 'C'), s)
c_pref = list(accumulate(list(c)))
skew = [g_pref[i] - c_pref[i] for i in range(len(s))]
min_skew = min(skew)
res = [i + 1 for i in range(len(skew)) if skew[i] == min_skew]
print(' '.join(map(str, res)))