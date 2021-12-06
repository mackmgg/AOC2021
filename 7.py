import clipboard

input = clipboard.get().split("\n\n")

numbers = input[0].split(",")
cards = []
called = []
winner = False

for i in range(1,len(input)):
	card = []
	for line in input[i].split("\n"):
		card.append([j for j in line.split(" ") if j])
	cards.append(card)

for number in numbers:
	called.append(number)
	for card in cards:
		if not winner:
			for card in cards:
				for line in card:
					if len([j for j in line if j in called]) >= 5:
						winner = card
				for i in range(5):
					column = []
					for line in card:
						column.append(line[i])
					if len([j for j in column if j in called]) >= 5:
						winner = card
	if winner:
		break

uncalledSum = 0
for line in winner:
	for number in line:
		if number not in called:
			uncalledSum += int(number)

print(uncalledSum*int(called[-1]))
