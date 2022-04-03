def dist(a, b):
    return sum(map(lambda pair: int(pair[0] != pair[1]), zip(a, b)))


s = input()
t = input()
d = int(input())

k = len(s)

k_mers = [t[i:i+k] for i in range(len(t) - k + 1)]

res = map(
    lambda k_mer_entry: str(k_mer_entry[0]),
    filter(
        lambda k_mer_entry: dist(s, k_mer_entry[1]) <= d,
        enumerate(k_mers)
    )
)

print(' '.join(res))