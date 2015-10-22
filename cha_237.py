# [2015-10-19] Challenge #237 [Easy] Broken Keyboard
def get_max_len_word(available_letters,word_list):
	max_len_word = ''
	for word in word_list:
		for letter in word:
			#print letter
			if letter not in available_letters:
				break
		else:
			if len(word) > len(max_len_word):
				max_len_word = word
	return max_len_word


if __name__ == '__main__':
	word_list = []
	f = open('data/enable1.txt','r')
	for line in f:
		word_list.append(line.strip())
	f.close()

	available_letters = []
	with open('data/in_cha237.txt') as f:
		for line in f:
			available_letters.append(line.strip())

	for letters in available_letters[1:]:
		print '{} = {}'.format(letters, get_max_len_word(letters,word_list))
	


