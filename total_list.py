#This program creates the totals of values in a list.

def main():
	#The list with the numbers to be added
	print "Enter the size of the List"
	size_list = input()
	number = [0] * size_list
	print ("Enter the Elements of the List")


	for x in range(size_list):
		number[x] = input()
		pass
	
	#The variable to hold the totals in a list
	total = 0;

	#Using a loop to add the values
	for x in number:
		total +=x
	
	average = total/size_list
	#Diplay the total value
	print "The size of the list is: ", len(number)

	print "The total: ", total

	print "The Average of Values in the Array are: ", average


main()