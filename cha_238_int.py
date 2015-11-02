#[2015-10-28] Challenge #238 [Intermediate] Fallout Hacking Game


def create_word_dict(word_list):
	max_len = max(len(x) for x in word_list)
	word_dictionary = dict()
	for number in range(1,max_len +1):
		word_dictionary[number] = []
	
	for word in word_list:
		word_dictionary[len(word)].append(word)
	return word_dictionary


def select_words(word_dictionary,l_word,n_word):
	return random.sample(word_dictionary[10],8)


def calculate_overlap(guess,correct):
	n_correct = 0
	for inx,letter in enumerate(guess):
		if letter == correct[inx]:
			n_correct = n_correct + 1
	return n_correct

#def play_game():
if __name__ == '__main__':
	import random

	word_list = []
	#read word_list
	with open('data/enable1.txt','r') as f:
		for line in f:
			word_list.append(line.strip())


	word_dic = create_word_dict(word_list)


	shown_words = select_words(word_dic,8,10)

	correct = shown_words[2]
	for word in shown_words:
		print correct
		print word
		print calculate_overlap(word,correct),'\n'




