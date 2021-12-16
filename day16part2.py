import clipboard
import numpy as np

transmission = clipboard.paste()
binary = bin(int(transmission, 16))[2:].zfill(len(transmission*4))

def processPackets(packets, length, lengthType):
	# print(packets)
	bitsProcessed = 0
	values = []
	if int(packets) != 0:
		if lengthType == '0':
			while bitsProcessed < length:
				# print(bitsProcessed)
				newValue, newBitsProcessed = processPacket(packets[bitsProcessed:], bitsProcessed)
				values.append(newValue)
				bitsProcessed = newBitsProcessed
				# print(bitsProcessed, length)
		else:
			for i in range(length):
				# print(bitsProcessed)
				newValue, newBitsProcessed = processPacket(packets[bitsProcessed:], bitsProcessed)
				values.append(newValue)
				bitsProcessed = newBitsProcessed
	else:
		bitsProcessed = len(packets)
	return values, bitsProcessed
	

def processPacket(packets, bitsProcessed = 0):
	# print(packets)
	if int(packets) != 0:
		type = int(packets[3:6], 2)
		if type == 4:
			# print(packets)
			i = 6
			number = ''
			while packets[i] == '1':
				number += packets[i+1:i+5]
				i += 5
			number += packets[i+1:i+5]
			value = int(number,2)
			bitsProcessed += i+5
		else:
			lengthType = packets[6]
			if lengthType == '0':
				nextLength = int(packets[7:22],2)
				nextBit = 22
			else:
				nextLength = int(packets[7:18],2)
				nextBit = 18
			values, newBitsProcessed = processPackets(packets[nextBit:], nextLength, lengthType)
			bitsProcessed += newBitsProcessed + nextBit
			if type == 0:
				value = np.sum(values)
			elif type == 1:
				value = np.prod(values)
			elif type == 2:
				value = np.min(values)
			elif type == 3:
				value = np.max(values)
			elif type == 5:
				value = 1 if values[0] > values[1] else 0
			elif type == 6:
				value = 1 if values[0] < values[1] else 0
			elif type == 7:
				value = 1 if values[0] == values[1] else 0
	else:
		bitsProcessed += len(packets)
			
	return value, bitsProcessed

versions, bitsProcessed = processPacket(binary)

print(versions)
