import itertools
import math

# 2d line: ax + by + c = 0  is  (a, b, c)

#          ax + by + c = 0     ((a, b, c),
# 3d line: dx + ez + f = 0  is  (d, e, f),
#          gy + hz + i = 0      (g, h, i))

dist = lambda p1, p2: sum((a - b)*(a - b) for a, b in zip(p1, p2))**0.5

pointsToLine2d = lambda p1, p2: (p2[1] - p1[1], p1[0] - p2[0], p1[1]*p2[0] - p1[0]*p2[1])

pointsToLines = lambda p1, p2: map(pointsToLine2d, itertools.combinations(p1, 2), itertools.combinations(p2, 2))

areParallel = lambda l1, l2: l1[0] * l2[1] == l2[0] * l1[1]

areSame = lambda l1, l2: areParallel(l1, l2) and (l1[1] * l2[2] == l2[1] * l1[2])

collinear = lambda p1, p2, p3: areSame(pointsToLine2d(p1, p2), pointsToLine2d(p2, p3))

intersect = lambda l1, l2: None if areParallel(l1, l2) else ((l2[1] * l1[2] - l1[1] * l2[2]) / (l2[0] * l1[1] - l1[0] * l2[1]),
                                                             (l1[0] * l2[2] - l1[2] * l2[0]) / (l2[0] * l1[1] - l1[0] * l2[1]))

rotate = lambda p, theta, origin=(0, 0): (origin[0] + (p[0] - origin[0]) * math.cos(theta) - (p[1] - origin[1]) * math.sin(theta),
                                          origin[1] + (p[0] - origin[0]) * math.sin(theta) + (p[1] - origin[1]) * math.cos(theta))
