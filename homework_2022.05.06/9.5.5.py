import sys
sys.setrecursionlimit(10000)

class Node:
	def __init__(self, id):
		self.id = id
		self.kids = dict()
		self.count = 0

	def minimise(self):
		new_kids = dict()
		for path, kid in self.kids.items():
			kid.minimise()
			if len(kid.kids) == 1:
				kid_path, kid_kid = list(kid.kids.items())[0]
				new_kids[path + kid_path] = kid_kid
			else:
				new_kids[path] = kid
		self.kids = new_kids

	def get_deepest_nonleaf(self):
		deepest = (0, '')
		for path, kid in self.kids.items():
			if len(kid.kids) == 0:
				continue
			cur_kid_deepest = kid.get_deepest_nonleaf()
			if cur_kid_deepest[0] + len(path) > deepest[0]:
				deepest = (cur_kid_deepest[0] + len(path), path + cur_kid_deepest[1])
		return deepest


	def list_edges(self):
		res = []
		for c, k in self.kids.items():
			res.append((self.id, k.id, c))
			res.extend(k.list_edges())
		return res
	

class Trie:
	root = Node(0)
	cur_id = 1

	def add_word(self, w):
		cur = self.root
		for c in w:
			if c not in cur.kids:
				cur.kids[c] = Node(self.cur_id)
				cur.is_leaf = False
				self.cur_id += 1
			cur = cur.kids[c]

	def get_longest_nonrepeat(self):
		return self.root.get_deepest_nonleaf()[1]

	def minimise(self):
		self.root.minimise()

	def __str__(self):
		return ' '.join(map(lambda item: item[2], self.root.list_edges()))

trie = Trie()

s = input() + '$'

for i in range(len(s)):
	trie.add_word(s[i:])

trie.minimise()

print(trie.get_longest_nonrepeat())
