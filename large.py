#python program to find the largest number among user inputs numbers

print("Ths program determines the largest number among the user entry: ")

x = 1
number = []
while x != -1:
	
	x = int(input("Enter the numbers to determine the largest or -1 to stop: "))
	number.append(x)

if(len(number) > 0):
	number.remove(-1)
	if(len(number) == 0):
		print("Your list was empty")
	else:
		print("=".center(60,"="))
		print("The list of numbers ", format(number))
		print ("The Largest Number in your list is, " + str(max(number)))
else:
	print("Your list was empty")

