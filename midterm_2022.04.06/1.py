# https://github.com/PennyroyalTea/bioinformatics-homeworks/blob/master/homework_2022.03.04/2.6.9.py

import math

c_to_id = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

def get_kmers(dna, k):
    return [dna[i:i + k] for i in range(len(dna) - k + 1)]


def gen_profile_matrix(kmers):
    k = len(kmers[0])
    res = [[0] * k for i in range(4)]
    for kmer in kmers:
        for i, c in enumerate(kmer):
            res[c_to_id[c]][i] += 1
    cnt = sum(map(lambda row: row[0] + 1, res))
    for c in range(4):
        res[c] = list(map(lambda val : (val + 1) / cnt, res[c]))
    return res


def get_score(kmer, profile_matrix):
    return math.prod(map(lambda pair: profile_matrix[c_to_id[pair[1]]][pair[0]], enumerate(kmer)))


def score_motifs(profile_matrix):
    k = len(profile_matrix[0])
    return sum(map(lambda i: sum(map(lambda row: entropy(row[i]), profile_matrix)), range(k)))


def entropy(x):
    return 0 if x < .000001 else -x * math.log2(x)

k, t = map(int, input().split())
dnas = input().split(' ')

best_score = 1e9
best_set = []

for motif1 in get_kmers(dnas[0], k):
    motifs = [motif1]
    for i in range(1, t):
        profile_matrix = gen_profile_matrix(motifs)
        cur_motif = max(map(lambda kmer: (get_score(kmer, profile_matrix), kmer), get_kmers(dnas[i], k)))[1]
        motifs.append(cur_motif)
    profile_matrix = gen_profile_matrix(motifs)
    if score_motifs(profile_matrix) < best_score:
        best_score = score_motifs(profile_matrix)
        best_set = motifs

print(' '.join(best_set))

