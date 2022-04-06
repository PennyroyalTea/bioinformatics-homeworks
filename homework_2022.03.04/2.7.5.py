import random
import math

ITERATIONS = 2000

c_to_id = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}


def get_kmers(dna, k):
    return [dna[i:i + k] for i in range(len(dna) - k + 1)]


def get_score(kmer, profile_matrix):
    return math.prod(map(lambda pair: profile_matrix[c_to_id[pair[1]]][pair[0]], enumerate(kmer)))


def score_motifs(profile_matrix):
    k = len(profile_matrix[0])
    return sum(map(lambda i: 1 - max(map(lambda row: row[i], profile_matrix)), range(k)))


def get_random_kmer(dna, k):
    pos = random.randint(0, len(dna) - k)
    return dna[pos:pos+k]


def get_random_kmers(dnas, k):
    return list(map(lambda dna: get_random_kmer(dna, k), dnas))


def motifs_to_matrix(kmers):
    k = len(kmers[0])
    res = [[0] * k for i in range(4)]
    for kmer in kmers:
        for i, c in enumerate(kmer):
            res[c_to_id[c]][i] += 1
    cnt = sum(map(lambda row: row[0] + 1, res))
    for c in range(4):
        res[c] = list(map(lambda val : (val + 1) / cnt, res[c]))
    return res


def matrix_to_motifs(matrix, dnas):
    k = len(matrix[0])
    res = list(map(
        lambda dna: min(
            map(
                lambda kmer: (get_score(kmer, matrix), kmer),
                get_kmers(dna, k)
            )
        )[1],
        dnas
    ))
    return res


k, t = map(int, input().split(' '))
dnas = list(map(lambda s: s.upper(), input().split(' ')))

best_score = 1e9
best_motifs = []

for iter in range(ITERATIONS):
    # print(f'iter {iter}')
    motifs = get_random_kmers(dnas, k)
    matrix = motifs_to_matrix(motifs)
    cur_best_score = score_motifs(matrix)
    # print(f'initial motifs: {motifs}\nmatrix:{matrix}\nscore:{cur_best_score}')
    cur_best_motifs = motifs
    while True:
        motifs = matrix_to_motifs(matrix, dnas)
        matrix = motifs_to_matrix(motifs)
        new_score = score_motifs(matrix)
        # print(f'new motifs: {motifs}\nmatrix:{matrix}\nscore:{new_score}')
        if new_score < cur_best_score:
            cur_best_score = new_score
            cur_best_motifs = motifs.copy()
        else:
            break
    if cur_best_score < best_score:
        best_score = cur_best_score
        best_motifs = cur_best_motifs.copy()

print(' '.join(best_motifs))