import clipboard
import numpy as np

syntax = clipboard.paste().splitlines()

score = 0

for line in syntax:
	expectedClosings = []
	for char in line:
		if char == '{':
			expectedClosings.append('}')
		elif char == '[':
			expectedClosings.append(']')
		elif char == '(':
			expectedClosings.append(')')
		elif char == '<':
			expectedClosings.append('>')
		elif char != expectedClosings.pop():	
			if char == '}':
				score += 1197
			if char == ']':
				score += 57
			if char == ')':
				score += 3
			if char == '>':
				score += 25137
			break

print(score)
