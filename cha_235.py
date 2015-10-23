#[2015-10-07] Challenge #235 [Easy] Ruth-Aaron Pairs


if __name__ == '__main__':
	pairs = []
	with open('data/in_cha235.txt','r') as f:
		f.readline()
		for line in f:
			pair = line.strip('()\n').split(',')
			pair = [int(x) for x in pair]
			pairs.append(pair)

	pair = pairs[0]
	
	num = pair[0]
	#def find_distinctive_prime_factor(num):

	prime_factors = []

	# def are_ruth_aaron(pair):




