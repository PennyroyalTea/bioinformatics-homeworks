from collections import Counter

s = input()
k, L, t = map(int, input().split(' '))

result = set()

l_intervals = [s[i:i+L] for i in range(len(s) - L)]

for l_interval in l_intervals:
    kmers = [l_interval[i:i+k] for i in range(len(l_interval) - k)]
    counter = Counter(kmers)
    lt_clumps = map(lambda entry: entry[0], filter(lambda entry: entry[1] >= t, counter.most_common()))
    result.update(lt_clumps)

print(' '.join(result))