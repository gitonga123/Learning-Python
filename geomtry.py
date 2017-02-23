# This program allows the user to choose various
# geomtry calculations from a menu. This program imports the circle and rectangle modules.
import circle
import rectangle

#constants for the menu choices
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
FIND_WIDTH_WITH_AREA = 6
FIND_WIDTH_WITH_PERIMETER = 5
QUIT_CHOICE = 7

#THE MAIN FUNCTION	
def main():
	# The choice variable controls the loop and holds 
	# the user's menu choice.
	choice = 0
	while choice != QUIT_CHOICE:
		#display the menu
		display_menu()

		#get the user's choice.
		choice = int(input("Enter your choice "))

		#perform the selected action.
		if choice == AREA_CIRCLE_CHOICE:
			radius = float(input("Enter the radius of the circle: "))
			print 'The area is ', circle.area(radius)
			print""
		elif choice == CIRCUMFERENCE_CHOICE:
			radius = float(input("Enter the circle's radius: "))
			print"The circumference is: ", circle.circumference(radius)
			print""
		elif choice == AREA_RECTANGLE_CHOICE:
			width = float(input("Enter the width of the rectangle: "))
			length = float(input("Enter the rectangle's length: "))
			print"Rectangle's Area = ", rectangle.area(width,length)
			print""
		elif choice == PERIMETER_RECTANGLE_CHOICE:
			width = float(input("Enter the width of the rectangle: "))
			length = float(input("Enter the rectangle's length: "))
			print"Rectangle's Perimeter  = ", rectangle.perimeter(width,length)	
			print""
		elif choice == FIND_WIDTH_WITH_PERIMETER:
			width = float(input("Enter the width or length of the rectangle: "))
			peri = float(input("Enter the perimeter of the rectangle: "))
			print"The length/width of the rectangle = ",rectangle.lengthwithperimeter(width,peri)
			print""
		elif choice == FIND_WIDTH_WITH_AREA:
			width = float(input("Enter the width or length of the rectangle: "))
			areas = float(input("Enter the Area of the rectangle: "))
			print"The length/width of the rectangle = ",rectangle.lengthwitharea(width,areas)
			print""
		elif choice == QUIT_CHOICE:
			print ("Existing the program ........")
		else:
			print('Error: Invalid selection.')

# The display_menu function displays a menu.
def display_menu():
	print('MENU')
	print('1. Area of a circle')
	print('2. Circumference of the circle')
	print('3. Area of a rectangle')
	print('4. Perimeter of a rectangle')
	print('5. Find the width or length of rectangle given perimeter')
	print('6. Find the width or length of rectangle given the area')
	print('7. QUIT')


main()