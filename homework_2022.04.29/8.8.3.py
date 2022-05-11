import sys
from math import dist

k, m = map(int, input().split(' '))

points = [list(map(float, line.strip().split(' '))) for line in sys.stdin]

centers = points[:k]

while True:
	# centers to clusters
	clusters = [[] for _ in range(k)]
	for point in points:
		closest_center_id, closest_center_dist = min(enumerate(centers), key = lambda p: dist(p[1], point))
		clusters[closest_center_id].append(point)

	# clusters to centers
	old_centers = centers[:] # to clone
	for i, cluster in enumerate(clusters):
		centers[i] = [sum(map(lambda c: c[axis], cluster)) / len(cluster) for axis in range(m)]

	if centers == old_centers:
		break

for center in centers:
	print(' '.join(map(lambda val: f'{val:.3f}', center)))