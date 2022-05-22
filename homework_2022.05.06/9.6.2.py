s = input()

suffixes = [(s[i:], i) for i in range(len(s))]

print(' '.join(map(lambda pair: str(pair[1]), sorted(suffixes))))