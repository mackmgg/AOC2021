import clipboard
import numpy as np

np.set_printoptions(linewidth=np.inf)

input = [i.splitlines() for i in clipboard.paste().split("\n\n")]
dots = [i.split(',') for i in input[0]]
insts = [i.split('fold along ') for i in input[1]]
insts = [i[1].split('=') for i in insts]

maxX = 0
maxY = 0
for dot in dots:
	if int(dot[0]) > maxX:
		maxX = int(dot[0])
	if int(dot[1]) > maxY:
		maxY = int(dot[1])

paper = np.zeros([maxY+1, maxX+1], dtype=int)

for dot in dots:
	paper[int(dot[1])][int(dot[0])] = 1

for inst in insts:
# if True:
# 	inst = insts[0]
	paper = np.split(paper, [int(inst[1]), int(inst[1])+1], 1 if inst[0] == 'x' else 0)
	# print(paper)
	maxY, maxX = paper[0].shape
	maxY2, maxX2 = paper[2].shape
	if inst[0] == 'y':
		for i in range(maxY2):
			for j in range(maxX2):
				paper[0][maxY-i-1][j] += paper[2][i][j]
	else:
		for i in range(maxY2):
			for j in range(maxX2):
				paper[0][i][maxX-j-1] += paper[2][i][j]
	paper = paper[0]


# for inst in insts[0]:
# if True:
# 	inst = insts[0]
# 	paper = np.split(paper, [int(inst[1])], 1 if inst[0] == 'x' else 0)
# 	print(paper)
# 	maxY1, maxX1 = paper[0].shape
# 	maxY2, maxX2 = paper[1].shape
# 	if inst[0] == 'y':
# 		if maxY1 > maxY2:
# 			paper = np.add(paper[0], np.pad(np.flipud(paper[1]), [(0,maxY1-maxY2),(0,0)]))
# 		else:
# 			paper = np.add(np.pad(paper[0], [(0,maxY2-maxY1),(0,0)], np.flipud(paper[1])))
# 	else:
# 		if maxX1 > maxX2:
# 			paper = np.add(paper[0], np.flipud(paper[1]))
# 		else:
# 			paper = np.add(paper[0], np.flipud(paper[1]))
# print(maxX, maxY)
# print(paper[0])
# print(paper[1])
paper[np.nonzero(paper)] = 1
print(paper)
# print(np.count_nonzero(paper))