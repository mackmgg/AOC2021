import clipboard
import numpy as np

displays = clipboard.paste().splitlines()

totalSum = 0

for display in displays:
	displayedDigits = ''
	
	line = display.split("|")
	inputs = line[0].split(" ")
	outputs = line[1].split(" ")
	
	digits = [None]*10
	digits[1] = set([i for i in inputs if len(i) == 2][0])
	digits[7] = set([i for i in inputs if len(i) == 3][0])
	digits[4] = set([i for i in inputs if len(i) == 4][0])
	fivedig = [set(i) for i in inputs if len(i) == 5]
	sixdig = [set(i) for i in inputs if len(i) == 6]
	digits[8] = set([i for i in inputs if len(i) == 7][0])
	for ind,i in enumerate(sixdig):
		if len(i.intersection(digits[1])) == 1:
			digits[6] = sixdig.pop(ind)
	for ind,i in enumerate(sixdig):
		if len(i.intersection(digits[4])) == 3:
			digits[0] = i
		else:
			digits[9] = i
	for ind,i in enumerate(fivedig):
		if len(i.intersection(digits[4])) == 2:
			digits[2] = fivedig.pop(ind)
	for ind,i in enumerate(fivedig):
		if len(i.intersection(digits[1])) == 1:
			digits[5] = i
		else:
			digits[3] = i
	
	
	for output in outputs:
		if len(output) > 0:
			digit = set(output)
			# print(digit)
			for i in range(10):
				if digit == digits[i]:
					displayedDigits += str(i)
					break
	
	totalSum += int(displayedDigits)
			
print(totalSum)