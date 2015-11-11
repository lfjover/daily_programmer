#[2015-11-09] Challenge #240 [Easy] Typoglycemia
import random

with open('data/input_cha240.txt','r') as f:
	words = []
	for line in f:
		words = words + line.strip().split()

def scramble(word):
	if len(word) ==1:
		return word
	else:
		middle = list(word[1:-1])
		random.shuffle(middle)
		middle = ''.join(middle)
		return word[0] + middle + word[-1]


scrambled_words = ' '.join([scramble(word) for word in words])
print scrambled_words