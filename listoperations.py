#This program demonstrates how the append method can be used
#to add items to a list.

def main():
	#first, create an empty list.
	name_list =[]

	#create a variable to control the loop
	again = 'y'

	#add some names to the list
	while again == 'y':
		#get a name from the user
		name = input('Enter a name: ')
		#Append the name to the list.
		name_list.append(name)

		#add another one?
		print("Do you want to add another name ?: ")
		again = input('Y = Yes, anything else = no! ')
		print()

		#display the names that were entered.
		print("here are the names you entered.")

		for name in name_list:
			print (name)
		pass
	pass
#This function demonstrates how to get the 
#index of an item in a list and then replaces
#that item when a new item
def index_list():
	#create a list with some items.
	food = ['Pizza','Burgers','Chips']

	#display the list
	print("Here are the items in the food list: ")
	print(food)

	#get the item to change
	item=input("Which item should I change ?: ")

	try:
		#Get the item's index in the list.
		item_index = food.index(item)

		#Get the value to replace it with.
		new_item = input('Enter the new value ')

		#Replace the old item woth the new item
		food[item_index] = new_item

		#display the list
		print("Here is the revised list: ")
		print(food)

	except ValueError:
		print "That item was not found in the list."
	pass

#This program demonstrates the insert method.
def insert_list():
	#create a list with some names
	names = ['James','Kathryn','Bill']

	#Display the list
	print("The list before the insert: ")
	print (names)

	#Insert a new name at element 0.
	names.insert(0,'Joe')

	#Display the list again
	print("the list after the insert: ")
	print(names)

	pass
#This function is used to sort items in a list
def sort():
	my_list = [12,6,7,13,6,9,0,3,4,56,43,1,3,12,43,12,45,56,78,88,99,0,89,93,64,56,16]
	print('Original order: ', my_list)
	my_list.sort()
	print("Ordered List: ", my_list)
	pass

#this function demonstrates how to use the remove method
#to remove an item from a list.
def remove():
	#create a list with some items.
	food = ['Pizza','Burgers','Chips','Tomato']
	#display the list
	print("Here are the items in the food list: ")
	print (food)

	#get the item to change.
	item = input("Which item should i remove? ")
	try:
		#remove the item
		food.remove(item)

		#display the list
		print("Here is the revised list: ")
		print (food)
	except ValueError:
		print("That item was not found in the list.")
	pass
#This method is used to reverse the item of a list
def reverse():
	my_list = [1,4,5,6,7,8,9,3,11,14]
	print("The orginal list is: ",my_list)
	my_list.reverse()
	print("Reversed list is: ", my_list)
	pass

#This method is used to delete a specific item in the list
def delfunction():
	my_list = [1,4,5,6,7,8,9,3,11,14]
	print("Before deletion: ", my_list)
	del my_list[8]
	print("After Deletion: ", my_list)
	pass

delfunction()