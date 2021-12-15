import clipboard
import numpy as np
import collections

input = [i.splitlines() for i in clipboard.paste().split("\n\n")]
template = input[0][0]
inserts = [i.split(' -> ') for i in input[1]]


currStep = template
for i in range(10):
	currPairs = np.array([])
	for j in range(len(currStep)-1):
		currPairs = np.append(currPairs, currStep[j] + currStep[j+1])
	for insert in inserts:
		if insert[0] in currPairs:
			currPairs[np.where(currPairs == insert[0])[0]] = insert[0][0] + insert[1] + insert[0][1]
	currStep = ''
	for pair in currPairs:
		currStep += pair[:2]
	currStep += currPairs[-1][2]

letters = collections.Counter(currStep).most_common()
print(letters[0][1] - letters[-1][1])