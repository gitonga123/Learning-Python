def collatz(number):
	if number % 2 == 0:
		print ("Even: ")
		return number / 2

	elif number % 2 ==1:
		print ("Odd: ")
		return 3 * number +1
	else:
		print ("Undefined")

print("Enter a number to check if its even or odd")
try:
	number = int(raw_input())

except ValueError:
	print ("Please enter a number: ")
	number = int(raw_input())

print (collatz(number))