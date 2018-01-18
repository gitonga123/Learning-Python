from __future__ import print_function

print ("This program displays a list of numbers and there squares" )

start = int(input("Enter the number to start with: "))
end = int(input("Enter the number to end with: "))

print()
print("Number\tSquare of the Number")
print("________________________________")

for number in range(start,end +1,):
	square_number = number**2
	print(number, "\t", square_number)
	pass