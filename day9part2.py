import clipboard
import numpy as np
from scipy.ndimage import measurements


array = [[0 if j=="9" else 1 for j in [*i]] for i in clipboard.paste().splitlines()]

labledBasins, numBasins = measurements.label(array)

basinSizes = []

for basin in range(1,numBasins+1):
	basinSizes.append(np.count_nonzero(labledBasins == basin))

sortedBasins = np.sort(basinSizes)

answer = sortedBasins[-1] * sortedBasins[-2] * sortedBasins[-3]

print(answer)	