# The circle module has function that performs calculations related to circles
import math

#The area function accepts a circle's radius as an argument
# and retrns the area of the circle

def area(radius):
	return math.pi* radius**2

def circumference(radius):
	return 2*math.pi * radius