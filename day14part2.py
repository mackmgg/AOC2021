import clipboard
import numpy as np
import collections

input = [i.splitlines() for i in clipboard.paste().split("\n\n")]
template = input[0][0]
inserts = [i.split(' -> ') for i in input[1]]


pairs = np.array([])
for j in range(len(template)-1):
	pairs = np.append(pairs, template[j] + template[j+1])
pairs = collections.Counter(pairs)

for i in range(40):
	nextPairs = collections.Counter()
	for insert in inserts:
		if insert[0] in pairs:
			count = pairs[insert[0]]
			nextPairs[insert[0][0] + insert[1]] += count
			nextPairs[insert[1] + insert[0][1]] += count
	pairs = nextPairs

letters = collections.Counter(template[-1])
for pair in pairs:
	letters[pair[0]] += pairs[pair]
				
letters = letters.most_common()
print(letters[0][1] - letters[-1][1])
