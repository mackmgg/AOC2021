import clipboard
import numpy as np

positions = [int(i) for i in clipboard.paste().split(",")]

minFuel = None
value = None

for i in range(np.amax(positions)):
	totalFuel = 0
	for position in positions:
		move = np.abs(position - i)
		totalFuel += move
	if minFuel is not None:
		if totalFuel < minFuel:
			minFuel = totalFuel
			value = i
	else:
		minFuel = totalFuel
		value = i
print(minFuel)
print(value)