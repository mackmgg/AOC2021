import clipboard
import numpy as np

array = np.array([[int(j) for j in [*i]] for i in clipboard.paste().splitlines()])

flashes = 0

for step in range(100):
	array = array + 1
	flashed = np.full_like(array,False)
	while np.max(array) > 9:
		for i in range(len(array)):
			for j in range(len(array[i])):
				if array[i][j] > 9:
					if not flashed[i][j]:
						flashes += 1
					flashed[i][j] = True
					array[i][j] = 0
					if i > 0 and i < len(array)-1:
						if j > 0 and j < len(array[i])-1:
							array[i-1][j] += 1
							array[i+1][j] += 1
							array[i][j-1] += 1
							array[i][j+1] += 1
							array[i+1][j+1] += 1
							array[i-1][j+1] += 1
							array[i+1][j-1] += 1
							array[i-1][j-1] += 1
						elif j > 0:
							array[i-1][j] += 1
							array[i+1][j] += 1
							array[i][j-1] += 1
							array[i+1][j-1] += 1
							array[i-1][j-1] += 1
						else:
							array[i-1][j] += 1
							array[i+1][j] += 1
							array[i][j+1] += 1
							array[i+1][j+1] += 1
							array[i-1][j+1] += 1
					elif i > 0:
						if j > 0 and j < len(array[i])-1:
							array[i-1][j] += 1
							array[i][j-1] += 1
							array[i][j+1] += 1
							array[i-1][j+1] += 1
							array[i-1][j-1] += 1
						elif j > 0:
							array[i-1][j] += 1
							array[i][j-1] += 1
							array[i-1][j-1] += 1
						else:
							array[i-1][j] += 1
							array[i][j+1] += 1
							array[i-1][j+1] += 1
					else:
						if j > 0 and j < len(array[i])-1:
							array[i+1][j] += 1
							array[i][j-1] += 1
							array[i][j+1] += 1
							array[i+1][j+1] += 1
							array[i+1][j-1] += 1
						elif j > 0:
							array[i+1][j] += 1
							array[i][j-1] += 1
							array[i+1][j-1] += 1
						else:
							array[i+1][j] += 1
							array[i][j+1] += 1
							array[i+1][j+1] += 1
	array[np.where(flashed)] = 0

print(flashes)