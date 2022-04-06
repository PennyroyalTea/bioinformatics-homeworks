import itertools


def gen_kmers(k):
    res = ['']
    for i in range(k):
        res = itertools.chain(*map(lambda kmer: list(map(lambda c: kmer + c, ['A', 'C', 'G', 'T'])), res))
    return list(res)


def dist_kmers(a, b):
    return len(list(filter(lambda pair: pair[0] != pair[1], zip(a, b))))


def dist_dna_kmer(dna, kmer):
    k = len(kmer)
    return min(map(lambda sub: dist_kmers(sub, kmer), [dna[i:i+k] for i in range(len(dna) - k + 1)]))


def dist_dnas_kmer(dnas, kmer):
    return sum(map(lambda dna: dist_dna_kmer(dna, kmer), dnas))


k = int(input())
dnas = input().split(' ')

all_kmers = gen_kmers(k)

best = int(1e9)
best_point = ''

for kmer in all_kmers:
    cur_dist = dist_dnas_kmer(dnas, kmer)
    if cur_dist < best:
        best = cur_dist
        best_point = kmer

print(best_point)