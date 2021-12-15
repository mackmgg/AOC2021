import clipboard
import numpy as np
import sys
from scipy.sparse.csgraph import shortest_path

input = clipboard.paste().splitlines()
for i in range(len(input)):
	input[i] = [int(i) for i in input[i]]

# distances = [sys.maxsize] * len(input) * len(input[0])
distanceMatrix = np.array([[0]*len(input[0])*(len(input))]*len(input)*(len(input[0])))

rowlen = len(input[0])

for i in range(len(input)):
	for j in range(rowlen):
		if i > 0 and i < len(input)-1:
			if j > 0 and j < rowlen-1:
				distanceMatrix[i*rowlen + j][i*rowlen + j - 1] = input[i][j-1]
				distanceMatrix[i*rowlen + j][i*rowlen + j + 1] = input[i][j+1]
				distanceMatrix[i*rowlen + j][(i-1)*rowlen + j] = input[i-1][j]
				distanceMatrix[i*rowlen + j][(i+1)*rowlen + j] = input[i+1][j]
			elif j > 0:
				distanceMatrix[i*rowlen + j][i*rowlen + j - 1] = input[i][j-1]
				distanceMatrix[i*rowlen + j][(i-1)*rowlen + j] = input[i-1][j]
				distanceMatrix[i*rowlen + j][(i+1)*rowlen + j] = input[i+1][j]
			else:
				distanceMatrix[i*rowlen + j][i*rowlen + j + 1] = input[i][j+1]
				distanceMatrix[i*rowlen + j][(i-1)*rowlen + j] = input[i-1][j]
				distanceMatrix[i*rowlen + j][(i+1)*rowlen + j] = input[i+1][j]
		elif i > 0:
			if j > 0 and j < rowlen-1:
				distanceMatrix[i*rowlen + j][i*rowlen + j - 1] = input[i][j-1]
				distanceMatrix[i*rowlen + j][i*rowlen + j + 1] = input[i][j+1]
				distanceMatrix[i*rowlen + j][(i-1)*rowlen + j] = input[i-1][j]
			elif j > 0:
				distanceMatrix[i*rowlen + j][i*rowlen + j - 1] = input[i][j-1]
				distanceMatrix[i*rowlen + j][(i-1)*rowlen + j] = input[i-1][j]
			else:
				distanceMatrix[i*rowlen + j][i*rowlen + j + 1] = input[i][j+1]
				distanceMatrix[i*rowlen + j][(i-1)*rowlen + j] = input[i-1][j]
		else:
			if j > 0 and j < rowlen-1:
				distanceMatrix[i*rowlen + j][i*rowlen + j - 1] = input[i][j-1]
				distanceMatrix[i*rowlen + j][i*rowlen + j + 1] = input[i][j+1]
				distanceMatrix[i*rowlen + j][(i+1)*rowlen + j] = input[i+1][j]
			elif j > 0:
				distanceMatrix[i*rowlen + j][i*rowlen + j - 1] = input[i][j-1]
				distanceMatrix[i*rowlen + j][(i+1)*rowlen + j] = input[i+1][j]
			else:
				distanceMatrix[i*rowlen + j][i*rowlen + j + 1] = input[i][j+1]
				distanceMatrix[i*rowlen + j][(i+1)*rowlen + j] = input[i+1][j]
				
# print(distanceMatrix)		
# print("Done!")
print(shortest_path(distanceMatrix)[0][-1])