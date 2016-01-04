# [2015-12-28] Challenge #247 [Easy] Secret Santa
import random

with open('data/cha_247.txt','r') as f:
	names = []
	for line in f:
		names.append(line.strip('/n').split())

giving = names
receiving_bag = [name for line in names for name in line] # flatten the list of names
for i_line,line in enumerate(giving):
	for person in line:
		receiving = person
		while receiving in line:
			receiving = random.choice(receiving_bag)  
		receiving_bag.remove(receiving)
		print '{} -> {}'.format(person,receiving)

