import clipboard
import numpy as np

array = [[int(j) for j in [*i]] for i in clipboard.paste().splitlines()]

riskLevel = 0

for i in range(len(array)):
	for j in range(len(array[i])):
		if i > 0 and i < len(array)-1:
			if j > 0 and j < len(array[i])-1:
				if array[i][j] < array[i-1][j] and array[i][j] < array[i+1][j] and array[i][j] < array[i][j-1] and array[i][j] < array[i][j+1]:
					riskLevel += array[i][j]+1
			elif j > 0:
				if array[i][j] < array[i-1][j] and array[i][j] < array[i+1][j] and array[i][j] < array[i][j-1]:
					riskLevel += array[i][j]+1
			else:
				if array[i][j] < array[i-1][j] and array[i][j] < array[i+1][j] and array[i][j] < array[i][j+1]:
					riskLevel += array[i][j]+1
		elif i > 0:
			if j > 0 and j < len(array[i])-1:
				if array[i][j] < array[i-1][j] and array[i][j] < array[i][j-1] and array[i][j] < array[i][j+1]:
					riskLevel += array[i][j]+1
			elif j > 0:
				if array[i][j] < array[i-1][j] and array[i][j] < array[i][j-1]:
					riskLevel += array[i][j]+1
			else:
				if array[i][j] < array[i-1][j] and array[i][j] < array[i][j+1]:
					riskLevel += array[i][j]+1
		else:
			if j > 0 and j < len(array[i])-1:
				if array[i][j] < array[i+1][j] and array[i][j] < array[i][j-1] and array[i][j] < array[i][j+1]:
					riskLevel += array[i][j]+1
			elif j > 0:
				if array[i][j] < array[i+1][j] and array[i][j] < array[i][j-1]:
					riskLevel += array[i][j]+1
			else:
				if array[i][j] < array[i+1][j] and array[i][j] < array[i][j+1]:
					riskLevel += array[i][j]+1
	
print(riskLevel)