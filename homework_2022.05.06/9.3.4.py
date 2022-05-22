class Node:
	def __init__(self, id):
		self.id = id
		self.kids = {
			'A': None,
			'T': None,
			'G': None,
			'C': None
		}

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
				self.cur_id += 1
			cur = cur.kids[c]

	def __str__(self):
		return '\n'.join(map(lambda item: ' '.join(map(str, item)), self.root.list_edges()))



trie = Trie()
for w in input().split(' '):
	trie.add_word(w)

print(trie)