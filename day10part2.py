import clipboard
import numpy as np

syntax = clipboard.paste().splitlines()

scores = []

for line in syntax:
	expectedClosings = []
	score = 0
	lineCorrupted = False
	for char in line:
		if char == '{':
			expectedClosings.append('}')
		elif char == '[':
			expectedClosings.append(']')
		elif char == '(':
			expectedClosings.append(')')
		elif char == '<':
			expectedClosings.append('>')
		elif char != expectedClosings[-1]:
			lineCorrupted = True
			break
		else:
			expectedClosings.pop()
	if lineCorrupted == False:
		for char in reversed(expectedClosings):
			score = score * 5
			if char == '}':
				score += 3
			if char == ']':
				score += 2
			if char == ')':
				score += 1
			if char == '>':
				score += 4
		scores.append(score)

print(np.median(scores))
