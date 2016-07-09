def main():
	first_name, last_name = inputs()
	result = show_sum(first_name, last_name)

	print "The sum of ", first_name , " and " ,  last_name , "  = ",result
	
def inputs():
	first = input ("Enter your first name: ")
	last = input("Enter your last name: ")
	return first, last


def show_sum(first, last):
	result = first + last
	return result


main()