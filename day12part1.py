import clipboard
import numpy as np

pathArray = [i.split("-") for i in clipboard.paste().splitlines()]

totalPaths = 0

def traversePath(pathsAndLocations, totalPaths):
	nextPaths = []
	for location, paths in pathsAndLocations:
		if location == "end":
			totalPaths += 1
		else:
			for path in paths:
				if path[0] == location:
					# print(path[1])
					if location.islower():
						# print([path[1], [i for i in paths if i[0] != location and i[1] != location]])
						nextPaths.append([path[1], [i for i in paths if i[0] != location and i[1] != location]])
					else:
						nextPaths.append([path[1], paths.copy()])
				if path[1] == location:
					if location.islower():
						nextPaths.append([path[0], [i for i in paths if i[0] != location and i[1] != location]])
					else:
						nextPaths.append([path[0], paths.copy()])
	return nextPaths, totalPaths

next = [["start", pathArray]]
while len(next) > 0:
	next, totalPaths = traversePath(next, totalPaths)
	# print(next)
print(totalPaths)
# 
# for point, path in traversePath([pathArray, "start"]):
# 	print(traversePath([path, point]))

