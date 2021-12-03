import clipboard

o2 = clipboard.get().splitlines()
co2 = o2.copy()

for i in range(len(o2[0])):
	totalO2 = 0
	totalCO2 = 0
	
	if len(o2) > 1:
		for line in o2:
			totalO2 += int(line[i])
		o2toRemove = '1' if totalO2 < len(o2)/2 else '0'
		print(o2toRemove)
		o2 = [j for j in o2 if j[i] != o2toRemove]
	
	if len(co2) > 1:
		for line in co2:
			totalCO2 += int(line[i])
		co2toRemove = '1' if totalCO2 >= len(co2)/2 else '0'
		co2 = [j for j in co2 if j[i] != co2toRemove]
		
rating = int(o2[0],2)*int(co2[0],2)
print(rating)
