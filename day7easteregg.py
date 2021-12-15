import clipboard
import numpy as np

positions = [int(i) for i in clipboard.paste().split(",")]

egg = ''

for position in positions:
	char = int(position)
	if char >= 32 and char <= 128:
		egg += chr(char)

print(egg)