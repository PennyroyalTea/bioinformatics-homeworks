def get_kmers(dna, k):
    return [dna[i:i+k] for i in range(len(dna) - k + 1)]


def get_neighbours(kmer, d):
    if kmer == '':
        return ['']
    if d == 0:
        return [kmer]
    res = []
    for c in 'ACGT':
        if kmer[0] == c:
            res.extend(map(lambda suf: c + suf, get_neighbours(kmer[1:], d)))
        else:
            res.extend(map(lambda suf: c + suf, get_neighbours(kmer[1:], d - 1)))
    return res


def appears_with_mismatches(target_kmer, dna, d):
    k = len(target_kmer)
    return any(map(lambda kmer: dist(target_kmer, kmer) <= d, get_kmers(dna, k)))


def dist(a, b):
    return len(list(filter(lambda pair: pair[0] != pair[1], zip(a, b))))


k, d = map(int, input().split(' '))
dnas = input().split(' ')

all_kmers = set()
for dna in dnas:
    all_kmers.update(get_kmers(dna, k))

answer = set()
for sub_kmer in all_kmers:
    for kmer in get_neighbours(sub_kmer, d):
        if all(map(lambda dna: appears_with_mismatches(kmer, dna, d), dnas)):
            answer.add(kmer)

print(' '.join(answer))