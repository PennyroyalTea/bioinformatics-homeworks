from collections import Counter

s = input()
k = int(input())

kmers = [s[i:i+k] for i in range(len(s) - k)]

counter = Counter(kmers)
max_count = counter.most_common(1)[0][1]
result = map(lambda tuple: tuple[0], filter(lambda counter_entry: counter_entry[1] == max_count, counter.most_common()))
print(' '.join(result))