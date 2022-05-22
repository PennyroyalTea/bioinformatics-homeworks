class Node:
	def __init__(self, id):
		self.id = id
		self.kids = {
			'A': None,
			'T': None,
			'G': None,
			'C': None
		}
		self.is_leaf = True

	def list_edges(self):
		res = []
		for c, k in self.kids.items():
			if k is None:
				continue
			res.append((self.id, k.id, c))
			res.extend(k.list_edges())
		return res
	

class Trie:
	root = Node(0)
	cur_id = 1

	def add_word(self, w):
		cur = self.root
		for c in w:
			if cur.kids[c] is None:
				cur.kids[c] = Node(self.cur_id)
				cur.is_leaf = False
				self.cur_id += 1
			cur = cur.kids[c]

	def match_prefix(self, prefix):
		cnt = 0
		cur = self.root
		for c in prefix:
			if cur.is_leaf:
				return prefix[:cnt]
			if cur.kids[c] is None:
				return False
			cur = cur.kids[c]
			cnt += 1
		if cur.is_leaf:
			return prefix[:cnt]
		else:
			return False

	def __str__(self):
		return '\n'.join(map(lambda item: ' '.join(map(str, item)), self.root.list_edges()))


pattern = input()
result = {}

trie = Trie()
for w in input().split(' '):
	trie.add_word(w)
	result[w] = []

for start_pos in range(len(pattern)):
	match_prefix_res = trie.match_prefix(pattern[start_pos:])
	if match_prefix_res:
		result[match_prefix_res].append(start_pos)

for w, indices in result.items():
	print(f'{w}: {" ".join(map(str, indices))}')
