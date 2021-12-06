import clipboard
import numpy as np

input = clipboard.paste().splitlines()

def getPoints(line):
	endpoints = line.split(" -> ")
	endpoint1 = endpoints[0].split(",")
	endpoint2 = endpoints[1].split(",")
	x1 = int(endpoint1[0])
	y1 = int(endpoint1[1])
	x2 = int(endpoint2[0])
	y2 = int(endpoint2[1])
	points = []
	if x1 == x2:
		for i in range(y1, y2+1):
			points.append([i, x1])
		for i in range(y2, y1+1):
			points.append([i, x1])

	elif y1 == y2:
		for i in range(x1, x2+1):
			points.append([y1, i])
		for i in range(x2, x1+1):
			points.append([y1, i])
	else:
		points = False
	return points

coordinates = np.zeros([1000,1000])

for line in input:
	points = getPoints(line)
	# print(points)
	if points:
		for point in points:
			coordinates[point[0],point[1]] += 1

print(np.count_nonzero(coordinates > 1))
# print(coordinates)