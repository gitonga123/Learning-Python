import coin

def main():
	my_coin = coin.Coin()

	print "The side of the coin that is up: ", my_coin.get_sideup();
	print "I am going to toss the coint in ten times:"

	for count in range(10):
		my_coin.toss()
		print(my_coin.get_sideup())

main()