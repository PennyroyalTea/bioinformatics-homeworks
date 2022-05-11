a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

def print_arr(a):
	print(' '.join(map(lambda x: f'{"+" if x > 0 else ""}{x}', a)))

for i in range(len(a)):
	cur_index = a.index(b[i]) if b[i] in a else a.index(-b[i])
	if cur_index != i:
		for j in range(i, cur_index + 1):
			a[j] *= -1
		a[i:cur_index + 1] = reversed(a[i:cur_index + 1])
		print_arr(a)
	if a[i] == -b[i]:
		a[i] = -a[i]
		print_arr(a)
	
