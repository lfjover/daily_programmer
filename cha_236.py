import random
pieces = ['O','I','S','Z','L','J','T']
print pieces

output = list(pieces) # creates a copy instead of pointing to the same one
random.shuffle(output)
for rounds in range(7):
	random.shuffle(pieces)
	output = output + pieces
	print output
output = ''.join(output)
print output[:50]