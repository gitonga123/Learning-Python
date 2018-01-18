#This program demonstrates the in operator used with a list.
def main():
	prod_nums = ['V457', 'F987','Q143','R688']

	#Get a product number to search for.
	search = input("Enter a number to search")

	#determine whether the product number is in the list.
	if search in prod_nums:
		print(search, " Was found in the list.")
	else:
		print (search, " was not found in the list.")
# call the main function
main()