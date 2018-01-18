import math

def main():
	a = float(input("Enter the length of side A"))
	b = float(input("Enter the length of side B"))

	c = math.hypot(a,b)

	print("The length of the hypotenous side is: ", c)


main()