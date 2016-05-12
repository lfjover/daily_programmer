from collections import Counter

edges_list = []
with open('data/cha_266.txt') as f:
	N = f.readline()
	for line in f:
		edges_list = edges_list + line.split()

edges = Counter([int(edge) for edge in edges_list])
for edge, number in edges.iteritems():
	print 'Node {} has a degree of {}'.format(edge,number) 
