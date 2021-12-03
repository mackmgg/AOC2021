import clipboard

routePlan = clipboard.get().splitlines()

forward = 0
depth = 0
aim = 0

for line in routePlan:
	plan = line.split(' ')
	if plan[0] == 'forward':
		forward += int(plan[1])
		depth += aim*int(plan[1])
	elif plan[0] == 'down':
		aim += int(plan[1])
	elif plan[0] == 'up':
		aim -= int(plan[1])
		
print(forward*depth)
