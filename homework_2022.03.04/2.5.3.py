import math

c_to_id = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}


def get_kmers(dna, k):
    return [dna[i:i+k] for i in range(len(dna) - k + 1)]


def get_score(kmer, profile_matrix):
    return math.prod(map(lambda pair: profile_matrix[c_to_id[pair[1]]][pair[0]], enumerate(kmer)))


s = input()
k = int(input())

profile_matrix = [list(map(float, input().split())) for i in range(4)]

print(max(map(lambda kmer: (get_score(kmer, profile_matrix), kmer), get_kmers(s, k)))[1])

