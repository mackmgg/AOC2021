import clipboard
import numpy as np

displays = clipboard.paste().splitlines()

uniqueDigits = 0

for display in displays:
	numbers = display.split("|")[1].split(" ")
	for number in numbers:
		if len(number) in [2, 3, 4, 7]:
			uniqueDigits += 1

print(uniqueDigits)