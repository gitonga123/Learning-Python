#This is a guess the number game
import random
secretNumber = random.randint(1,20)
print('AM thinking of a number between 1 and 20.')

for guesses in range(1,7):
	print('Take a guess')
	guess = int(input())

	if guess < secretNumber:
		print('Your guess is too low.')
	elif guess > secretNumber:
		print('Your guess is to high.')
	else:
		break

if guess == secretNumber:
	print('Good Job! You guessed my number in ' + str(guesses) + ' Guesses!')
else:
	print('The number of trials are over')
	print('Nope. The number i was thinking of was ' + str(secretNumber))