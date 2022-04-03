def dist(a, b):
    return sum(map(lambda pair: int(pair[0] != pair[1]), zip(a, b)))


pattern = input()
text = input()
d = int(input())

k = len(pattern)
k_mers = [text[i:i+k] for i in range(len(text) - k + 1)]

print(len(list(filter(lambda k_mer: dist(pattern, k_mer) <= d, k_mers))))