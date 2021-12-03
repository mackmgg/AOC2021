import clipboard

debug = clipboard.get().splitlines()

totals = [0]*len(debug[0])
mostCommon = []
leastCommon = []
for line in debug:
	for i in range(len(line)):
		totals[i] += int(line[i])

for total in totals:
	if total > len(debug)/2:
		mostCommon.append(1)
		leastCommon.append(0)
	else:
		mostCommon.append(0)
		leastCommon.append(1)
		
print(mostCommon)
print(leastCommon)
