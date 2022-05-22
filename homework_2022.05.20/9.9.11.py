def add_indices(s):
	count = dict()
	res = []
	for c in s:
		if not c in count:
			count[c] = 0
		res.append((c, count[c]))
		count[c] += 1
	return res

s = input()

last_column = add_indices(s)
first_column = add_indices(sorted(s))

prev = ('$', 0)
restored = ''

for i in range(len(s)):
	cur = first_column[last_column.index(prev)]
	restored += cur[0]
	prev = cur

print(restored)