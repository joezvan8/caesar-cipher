import sys

shift_amt = int(sys.argv[1])

message = []
for line in sys.stdin:
	line = line.upper()
	changed_line = []
	for char in line:
		if char.isalpha():
			changed_line.append(char)
		line = "".join(changed_line)
	message.append(line)

for line in message:
	for char in line:
		char += shift_amt	

