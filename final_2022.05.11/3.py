# from: https://github.com/PennyroyalTea/bioinformatics-homeworks/blob/master/homework_2022.04.29/8.8.3.py

import sys
import random
from math import dist


k, m = map(int, input().split(' '))

points = [list(map(float, line.strip().split(' '))) for line in sys.stdin]

def choice_weighted_with_replace(a, weights):
	if not weights:
		v = random.choice(a)
	else:
		weights_sum = sum(weights)
		weights = list(map(lambda w: w / weights_sum, weights))
		r = random.uniform(0, 1)
		s = 0
		for i, w in enumerate(weights):
			s += w
			if s > r:
				v = a[i]
				break
	a.remove(v)
	return v

def kmeans_init(points, k):
	points = points[:] # cloning
	centers = [choice_weighted_with_replace(points, None)]
	for _ in range(k - 1):
		weights = list(map(
			lambda point: dist(point, min(centers, key=lambda center: dist(center, point)))**2, 
				points))
		print(f'points: {points}')
		print(f'weights: {weights}')
		centers.append(choice_weighted_with_replace(points, weights))
	return centers

centers = kmeans_init(points, k)

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
