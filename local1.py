#Definitiona of the main function
def main():
	get_name()
	print('Hello', name)	#this causes an error
	

def get_name():
	name = input('Enter your name: ')
	

#call the main function
main()

#This program will return an Error since the main function
#is trying to access the get_name local variable