import sys

shift_amt = int(sys.argv[1])

message = []
line = sys.stdin.readline()	
line = line.upper()
changed_line = []	

for char in line:
	if char.isalpha():
		changed_line.append(char)
		
line = "".join(changed_line)
message.append(line)

encoded_message = []

for line in message:
	for char in line:
		shifted = (ord(char) - ord('A') + shift_amt) % 26 + ord('A')
		encoded_message.append(chr(shifted))

encoded_message = "".join(encoded_message)

block_count = 0

for i in range(0, len(encoded_message), 5):
	block = encoded_message[i:i+5]
	print(block, end=" ")

	block_count += 1
	if block_count == 10:
		print()
		block_count = 0


if block_count != 0:
	print()















