def better_bw_matching(first_occurrence, last_column, pattern, count):
	top = 0
	bottom = len(last_column) - 1
	while top <= bottom:
		if len(pattern) == 0:
			return bottom - top + 1
		c = pattern.pop()
		if c in last_column[top:bottom + 1]:
			top = first_occurrence[c] + count[c][top]
			bottom = first_occurrence[c] + count[c][bottom + 1] - 1
		else:
			return 0

s = input()

first_occurrence = dict()

s_f = sorted(s)
for i, c in enumerate(s_f):
	if not c in first_occurrence:
		first_occurrence[c] = i

count = dict()

uniq_s = list(set(s))

for c in uniq_s:
	count[c] = [0] * (len(s) + 1)

for i in range(1, len(s) + 1):
	for c in uniq_s:
		count[c][i] = count[c][i - 1]
	count[s[i - 1]][i] += 1

print(' '.join(map(
	lambda pattern: str(better_bw_matching(first_occurrence, s, list(pattern), count)), 
	input().split(' '))))

