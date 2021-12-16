import clipboard
import numpy as np

transmission = clipboard.paste()
binary = bin(int(transmission, 16))[2:].zfill(len(transmission*4))

def processPackets(packets, length, lengthType):
	# print(packets)
	versions = 0
	bitsProcessed = 0
	if int(packets) != 0:
		if lengthType == '0':
			while bitsProcessed < length:
				# print(bitsProcessed)
				newVersions, newBitsProcessed = processPacket(packets[bitsProcessed:], bitsProcessed)
				versions += (newVersions)
				bitsProcessed = newBitsProcessed
				# print(bitsProcessed, length)
		else:
			for i in range(length):
				# print(bitsProcessed)
				newVersions, newBitsProcessed = processPacket(packets[bitsProcessed:], bitsProcessed)
				versions += (newVersions)
				bitsProcessed = newBitsProcessed
	else:
		bitsProcessed = len(packets)
	return versions, bitsProcessed
	

def processPacket(packets, bitsProcessed = 0):
	# print(packets)
	versions = 0
	if int(packets) != 0:
		versions += (int(packets[0:3], 2))
		type = int(packets[3:6], 2)
		if type == 4:
			# print(packets)
			i = 6
			number = ''
			while packets[i] == '1':
				number += packets[i+1:i+5]
				i += 5
			number += packets[i+1:i+5]
			# print(number)
			# print(int(number,2))
			bitsProcessed += i+5
		else:
			lengthType = packets[6]
			if lengthType == '0':
				nextLength = int(packets[7:22],2)
				nextBit = 22
			else:
				nextLength = int(packets[7:18],2)
				nextBit = 18
			newVersions, newBitsProcessed = processPackets(packets[nextBit:], nextLength, lengthType)
			bitsProcessed += newBitsProcessed + nextBit
			versions += (newVersions)
	else:
		bitsProcessed += len(packets)
			
	return versions, bitsProcessed

versions, bitsProcessed = processPacket(binary)

print(versions)
