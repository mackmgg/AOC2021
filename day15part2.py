import clipboard
import numpy as np
import sys
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import dok_matrix

input = clipboard.paste().splitlines()
for i in range(len(input)):
	input[i] = [int(i) for i in input[i]]
original = np.array(input)
hor = original.copy()
for i in range(1,5):
	hor = np.append(hor, original+(i), axis=0)
input = hor.copy()
for i in range(1,5):
	input = np.append(input, hor+(i), axis=1)

while np.amax(input) > 9:
	input[np.where(input > 9)] -= 9

# distances = [sys.maxsize] * len(input) * len(input[0])
matrixDimension = len(input)*len(input[0])
distanceMatrix = dok_matrix((matrixDimension,matrixDimension), dtype=int)
# distanceMatrix = np.array([[0]*len(input[0])*(len(input))]*len(input)*(len(input[0])))
rowlen = len(input[0])

for i in range(len(input)):
	for j in range(rowlen):
		if i > 0 and i < len(input)-1:
			if j > 0 and j < rowlen-1:
				distanceMatrix[i*rowlen + j,i*rowlen + j - 1] = input[i][j-1]
				distanceMatrix[i*rowlen + j,i*rowlen + j + 1] = input[i][j+1]
				distanceMatrix[i*rowlen + j,(i-1)*rowlen + j] = input[i-1][j]
				distanceMatrix[i*rowlen + j,(i+1)*rowlen + j] = input[i+1][j]
			elif j > 0:
				distanceMatrix[i*rowlen + j,i*rowlen + j - 1] = input[i][j-1]
				distanceMatrix[i*rowlen + j,(i-1)*rowlen + j] = input[i-1][j]
				distanceMatrix[i*rowlen + j,(i+1)*rowlen + j] = input[i+1][j]
			else:
				distanceMatrix[i*rowlen + j,i*rowlen + j + 1] = input[i][j+1]
				distanceMatrix[i*rowlen + j,(i-1)*rowlen + j] = input[i-1][j]
				distanceMatrix[i*rowlen + j,(i+1)*rowlen + j] = input[i+1][j]
		elif i > 0:
			if j > 0 and j < rowlen-1:
				distanceMatrix[i*rowlen + j,i*rowlen + j - 1] = input[i][j-1]
				distanceMatrix[i*rowlen + j,i*rowlen + j + 1] = input[i][j+1]
				distanceMatrix[i*rowlen + j,(i-1)*rowlen + j] = input[i-1][j]
			elif j > 0:
				distanceMatrix[i*rowlen + j,i*rowlen + j - 1] = input[i][j-1]
				distanceMatrix[i*rowlen + j,(i-1)*rowlen + j] = input[i-1][j]
			else:
				distanceMatrix[i*rowlen + j,i*rowlen + j + 1] = input[i][j+1]
				distanceMatrix[i*rowlen + j,(i-1)*rowlen + j] = input[i-1][j]
		else:
			if j > 0 and j < rowlen-1:
				distanceMatrix[i*rowlen + j,i*rowlen + j - 1] = input[i][j-1]
				distanceMatrix[i*rowlen + j,i*rowlen + j + 1] = input[i][j+1]
				distanceMatrix[i*rowlen + j,(i+1)*rowlen + j] = input[i+1][j]
			elif j > 0:
				distanceMatrix[i*rowlen + j,i*rowlen + j - 1] = input[i][j-1]
				distanceMatrix[i*rowlen + j,(i+1)*rowlen + j] = input[i+1][j]
			else:
				distanceMatrix[i*rowlen + j,i*rowlen + j + 1] = input[i][j+1]
				distanceMatrix[i*rowlen + j,(i+1)*rowlen + j] = input[i+1][j]

# print(distanceMatrix)		
# print("Done!")
print(shortest_path(distanceMatrix, indices=0)[-1])