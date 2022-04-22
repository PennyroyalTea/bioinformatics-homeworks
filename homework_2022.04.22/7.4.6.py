def find_path(g, x, y):
    """finds path in a tree g from vertex x to y (there is exactly one path because g is a tree)
        !!! the path doesnt include x and goes in reversed order
    """
    # dfs to build a path
    def dfs(v, visited, target):
        visited[v] = True
        for u, weight, valid in g[v]:
            if not valid:
                continue
            if u == target:
                return True, [(u, weight)]
            if visited[u]:
                continue
            res = dfs(u, visited, target)
            if res[0]:
                res[1].append((u, weight))
                return res
        return False, []

    return dfs(x, [False] * len(g), y)[1]


def get_tree(a, cur_n):
    if cur_n == 2:
        g = [[] for _ in range(n)]
        g[0] = [[1, a[0][1], True]]
        g[1] = [[0, a[1][0], True]]
        return g
    # calculate limb
    limb = (a[0][cur_n - 1] + a[1][cur_n - 1] - a[0][1]) // 2
    for i in range(cur_n - 1):
        for j in range(cur_n - 1):
            if i == j:
                continue
            cur_limb = (a[i][cur_n - 1] + a[j][cur_n - 1] - a[i][j]) // 2
            if cur_limb < limb:
                limb = cur_limb

    # substract limb from last row / col
    for i in range(cur_n - 1):
        a[i][cur_n - 1] -= limb
        a[cur_n - 1][i] -= limb

    # (v, u) path is location of last leaf connection
    v, u = -1, -1
    for i in range(cur_n - 1):
        for j in range(cur_n - 1):
            if i == j:
                continue
            if a[cur_n - 1][i] + a[cur_n - 1][j] == a[i][j]:
                v, u = i, j
                break

    x = a[v][cur_n - 1]

    # recursively get smaller tree
    tree = get_tree(a, cur_n - 1)

    # find (or add) node w on distance x between v and u
    path = find_path(tree, v, u)
    cur_dist, cur_v = 0, v
    prev_dist, prev_v = -1, -1
    while cur_dist < x:
        last_u, last_weight = path.pop()
        prev_dist = cur_dist
        cur_dist += last_weight
        prev_v = cur_v
        cur_v = last_u

    # there is no parent node in the tree yet
    if cur_dist > x:
        vertex_to_add = len(tree)
        tree.append([])
        # remove edge (prev_v, cur_v)
        for i in range(len(tree[prev_v])):
            if tree[prev_v][i][0] == cur_v and tree[prev_v][i][2]:
                tree[prev_v][i][2] = False
                break
        for i in range(len(tree[cur_v])):
            if tree[cur_v][i][0] == prev_v and tree[cur_v][i][2]:
                tree[cur_v][i][2] = False
                break
        # add edges (prev_v, vertex_to_add) and (cur_v, vertex_to_add)
        tree[prev_v].append([vertex_to_add, x - prev_dist, True])
        tree[vertex_to_add].append([prev_v, x - prev_dist, True])
        tree[cur_v].append([vertex_to_add, cur_dist - x, True])
        tree[vertex_to_add].append([cur_v, cur_dist - x, True])
        cur_v = vertex_to_add

    # connect (curn-1) leaf to cur_v node
    tree[cur_v].append([cur_n - 1, limb, True])
    tree[cur_n - 1].append([cur_v, limb, True])

    return tree


n = int(input())

a = [[int(x) for x in input().split(' ')] for _ in range(n)]

t = get_tree(a, n)

for v, v_neighbours in enumerate(t):
    for u, weight, valid in v_neighbours:
        if valid:
            print(f'{v}->{u}: {weight}')