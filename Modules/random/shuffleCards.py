from random import shuffle
from pprint import pprint
def main():
	values = range(1,11) + 'Jack Queen King'.split()
	suits = 'diamonds clubs hearts spades'.split()
	# functional programming style(one for loop embeded in another loop)
	deck = ['%s of %s' % (v, s) for v in values for s in suits]
	shuffle(deck)
	pprint(deck)

if __name__ == '__main__':
	main()
