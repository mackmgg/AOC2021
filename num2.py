import clipboard

sonarData = clipboard.get().splitlines()

numIncreases = 0

for i in range(len(sonarData) - 3):
	if int(sonarData[i]) < int(sonarData[i+3]):
		numIncreases += 1
		
print(numIncreases)
