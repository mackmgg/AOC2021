import clipboard
import numpy as np

pathArray = [i.split("-") for i in clipboard.paste().splitlines()]

totalPaths = 0

def traversePath(pathsAndLocations, totalPaths):
	nextPaths = []
	for location, paths, visited, canVisit, prev in pathsAndLocations:
		if location == "end":
			totalPaths += 1
			# print(prev + [location])
		else:
			for path in paths:
				if path[0] == location:
					if location == "start":
						nextPaths.append([path[1], [i for i in paths if i[0] != location and i[1] != location], visited, canVisit, prev + [location]])
					elif location.islower() and (visited.count(location) == True and canVisit == True):
						nextPaths.append([path[1], [i for i in paths if i[0] != location and i[1] != location], visited, False, prev + [location]])
					elif location.islower() and not visited.count(location):
						nextPaths.append([path[1], paths.copy(), visited + [location], canVisit, prev + [location]])
					elif not visited.count(location):
						nextPaths.append([path[1], paths.copy(), visited, canVisit, prev + [location]])
				if path[1] == location:
					if location == "start":
						nextPaths.append([path[0], [i for i in paths if i[0] != location and i[1] != location], visited, canVisit, prev + [location]])
					elif location.islower() and (visited.count(location) == True and canVisit == True):
						nextPaths.append([path[0], [i for i in paths if i[0] != location and i[1] != location], visited, False, prev + [location]])
					elif location.islower() and not visited.count(location):
						nextPaths.append([path[0], paths.copy(), visited + [location], canVisit, prev + [location]])
					elif not visited.count(location):
						nextPaths.append([path[0], paths.copy(), visited, canVisit, prev + [location]])
	return nextPaths, totalPaths

next = [["start", pathArray, [], True, []]]
while len(next) > 0:
	next, totalPaths = traversePath(next, totalPaths)
	# print(next)
print(totalPaths)
