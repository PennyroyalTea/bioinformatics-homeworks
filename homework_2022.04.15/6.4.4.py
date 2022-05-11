a = list(map(int, input().split(' ')))

def print_arr(a):
	print(' '.join(map(lambda x: f'{"+" if x > 0 else ""}{x}', a)))

for i in range(len(a)):
	cur_index = a.index(i + 1) if (i + 1) in a else a.index(-(i + 1))
	if cur_index != i:
		for j in range(i, cur_index + 1):
			a[j] *= -1
		a[i:cur_index + 1] = reversed(a[i:cur_index + 1])
		print_arr(a)
	if a[i] < 0:
		a[i] = -a[i]
		print_arr(a)
	
