import itertools


n = int(input())
D = [[int(x) for x in input().strip().split(' ')] for _ in range(n)]


def distance(c1, c2, cluster_to_elements):
    res = 0
    cnt = 0
    for v1 in cluster_to_elements[c1]:
        for v2 in cluster_to_elements[c2]:
            res += D[v1][v2]
            cnt += 1
    return res / cnt


def UPGMA(D, n):
    clusters = list(range(n))
    cluster_to_elements = dict(enumerate(map(lambda t: [t], range(n))))
    g = [[] for _ in range(n)]
    valid = [True] * n
    age = [0] * n
    last_id = n
    while len(clusters) > 1:
        # find closest clusters
        best_distance = distance(clusters[0], clusters[1], cluster_to_elements)
        c1, c2 = clusters[0], clusters[1]
        for c_1, c_2 in itertools.combinations(clusters, r=2):
            if distance(c_1, c_2, cluster_to_elements) < best_distance:
                best_distance = distance(c_1, c_2, cluster_to_elements)
                c1, c2 = c_1, c_2

        # merge em
        cluster_to_elements[last_id] = []
        cluster_to_elements[last_id].extend(cluster_to_elements[c1])
        cluster_to_elements[last_id].extend(cluster_to_elements[c2])

        clusters.remove(c1)
        clusters.remove(c2)
        clusters.append(last_id)

        valid[c1] = False
        valid[c2] = False
        valid.append(True)

        # add it to g
        g.append([])
        g[-1].extend([c1, c2])
        g[c1].append(last_id)
        g[c2].append(last_id)

        age.append(D[c1][c2] / 2)
        # update matrix D
        for row_id, row in enumerate(D):
            if not valid[row_id]:
                row.append(-1)
                continue
            c1_sz, c2_sz = len(cluster_to_elements[c1]), len(cluster_to_elements[c2])
            new_distance = (D[c1][row_id] * c1_sz + D[c2][row_id] * c2_sz) / (c1_sz + c2_sz)
            row.append(new_distance)
        D.append(list(map(lambda j: D[j][last_id], range(last_id))) + [0])
        last_id += 1

    # calculate distances from D and ages
    def dfs(v, visited):
        visited[v] = True
        for u in g[v]:
            if visited[u]:
                continue
            dfs(u, visited)
            print(f'{v}->{u}: {age[v] - age[u]}')
            print(f'{u}->{v}: {age[v] - age[u]}')

    dfs(clusters[0], [False] * last_id)


UPGMA(D, n)
