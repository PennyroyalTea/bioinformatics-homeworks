compliment = {
    'G': 'C',
    'T': 'A',
    'C': 'G',
    'A': 'T'
}


def rc(pattern):
    return (''.join(map(lambda c: compliment[c], pattern)))[::-1]


def dist(a, b):
    return sum(map(lambda pair: int(pair[0] != pair[1]), zip(a, b)))


def d_neighbours(s, d):
    if d == 0 or len(s) == 0:
        return [s]
    res = []
    for c0 in ['G', 'T', 'C', 'A']:
        if c0 == s[0]:
            res.extend(list(map(lambda res: c0 + res, d_neighbours(s[1:], d))))
        else:
            res.extend(list(map(lambda res: c0 + res, d_neighbours(s[1:], d - 1))))
    return res


s = input()
k, d = map(int, input().split(' '))

k_mers = [s[i:i+k] for i in range(len(s) - k + 1)]

candidates = set()

for k_mer in k_mers:
    neighbours = d_neighbours(k_mer, d)
    candidates.update(neighbours)
    neighbours = d_neighbours(rc(k_mer), d)
    candidates.update(neighbours)

best_cnt = -1
best_res = []

for cur in candidates:
    cnt_pattern = len(list(filter(lambda k_mer: dist(cur, k_mer) <= d, k_mers)))
    cnt_pattern_rc = len(list(filter(lambda k_mer: dist(rc(cur), k_mer) <= d, k_mers)))
    cnt_all = cnt_pattern_rc + cnt_pattern
    if cnt_all > best_cnt:
        best_cnt = cnt_all
        best_res = [cur]
    elif cnt_all == best_cnt:
        best_res.append(cur)

print(' '.join(best_res))