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
		if len(cards) > 1:
			for card in cards:
				for line in card:
					if len([j for j in line if j in called]) >= 5:
						if card in cards:
							cards.remove(card)
						break
				for i in range(5):
					column = []
					for line in card:
						column.append(line[i])
					if len([j for j in column if j in called]) >= 5:
						if card in cards:
							cards.remove(card)
	if len(cards) == 1:
		if not winner:
			for card in cards:
					for line in card:
						if len([j for j in line if j in called]) >= 5:
							winner = True
					for i in range(5):
						column = []
						for line in card:
							column.append(line[i])
						if len([j for j in column if j in called]) >= 5:
							winner = True
	if winner:
		break


print(cards)
print(called)

uncalledSum = 0
for line in cards[0]:
	for number in line:
		if number not in called:
			uncalledSum += int(number)

print(uncalledSum*int(called[-1]))
