# This program demonstrates two functions that 
# have local variables with the same name

def main():
	#call the texas function
	texas()
	# call the california function
	california()
	pass

#Defintion of the texas function. It creates
# a local variable named birds.

def texas():
	birds = 5000
	print('Texas has', birds, ' Birds')
	pass

#Definition of the california function. It a
# creates a local variable named birds
def california():
	birds = 8000
	print('California has', birds, ' Birds')
	pass

# Call the main function
main()