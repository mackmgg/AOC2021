import clipboard
import numpy as np

fish = [int(i) for i in clipboard.paste().split(",")]


for i in range(80):
	for f in range(len(fish)):
		if fish[f] > 0:
			fish[f] -= 1
		else:
			fish[f] = 6
			fish.append(8)

print(len(fish))
