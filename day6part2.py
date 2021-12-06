import clipboard
import numpy as np

fishDays = [int(i) for i in clipboard.paste().split(",")]
fishBorn = np.ones(len(fishDays))

for i in range(256):
	fishDays = np.subtract(fishDays, 1)
	newBirths = np.where(fishDays < 0)
	numNewBirths = np.sum(fishBorn[newBirths])
	if numNewBirths > 0:
		fishDays = np.append(fishDays, 8)
		fishBorn = np.append(fishBorn, numNewBirths)
	fishDays[newBirths] = 6	

print(np.sum(fishBorn))

# print(len(fish))
