# A Class is a description of an object's characteristics.
#An object is an istance of a class. Instance means a representation 
import random
#the Coin class simulates a coin that can be flipped.
class Coin:
	#The __init__ method initializes the sideup datat attribute with 'Heads'
	def __init__(self):
		self.sideup = 'Heads'
		#The toss method generates a random number in the
		#range of 0 through 1. If the number is 0, then sideup is set to 'Heads'.
		#Otherwise, sideup is set to 'Trails'
		pass

	def toss(self):
		if random.randint(0,1) == 0:
			self.sideup = 'Heads'
		else:
			self.sideup = 'Tails'
			
		pass

	def get_sideup(self):
		return self.sideup
		pass


def main():
	my_coin = Coin()
	print('This side is up: ', my_coin.get_sideup())

	#Toss the coin
	print("I am tossing the coin ...")
	my_coin.toss()

	print('This side is up:', my_coin.get_sideup())


main()