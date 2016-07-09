# This program demonstrates an argument being
# passed to a function

def main():
	value = input('Enter any number: ')
	show_double(value)
	pass

#The show_double function accepts an argument
# and displays double its value
def show_double(number):
	value = input('Enter the number to multiply with: ')
	result = number * value
	print result
	pass

# Call the main function
main()