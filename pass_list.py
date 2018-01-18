#This program uses a function to calculate the
# total of the values in a list

def main():
	#create a List
	numbers = [2,4,6,8,10]
	#Display the total of the list elements
	print "The total is ", get_total(numbers)

	numberz = get_values()
	#Display the values in the list
	print "The numbers in the list are: ", numberz
#the Get total function accepts a list as an
#argument returns the total of the values in the list
def get_total(value_list):
	#create a variable to use as an accumulator
	total = 0

	#Calculate the total of the list elements

	for values in value_list:
		total += values
	
	return total
#This function returns a reference to the list
#From the user and stores them in a list. The
# function returns a reference to the list
def get_values():
	# Create an empty list.
	values = []

	#create a variable to control the loop
	again = 'y'

	#Get values from the user and add them to the list
	while again == 'y':
		#Get a number and add it to the list.
		num = int(input("Enter a number: "))
		values.append(num)


		print "Do you want to add another number"
		again = input("y = Yes, anything else = no: ")
		again = str(again)
		print
		pass
		#Return the list
		return values
	pass


main()	

