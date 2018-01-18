def area(width, length):
	return width * length

def perimeter(width, length):
	return 2* (width + length)

def lengthwitharea(width, area):
	return area / width
	
def lengthwithperimeter(width, perimeter):
	width = width * 2
	return (perimeter - width)/2
	
