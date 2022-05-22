def dist(s1, s2):
	return len(list(filter(lambda p: p[0] != p[1], zip(s1, s2))))

s = input()

patterns = input().split(' ')

d = int(input())

for it, pattern in enumerate(patterns):
	ids = []
	for i in range(len(s) - len(pattern) + 1):
		if dist(s[i:i+len(pattern)], pattern) <= d:
			ids.append(i)
	print(f'{pattern}: {" ".join(map(str, ids))}')