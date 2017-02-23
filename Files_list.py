
#This program uses the writelines method to save
# a list of strings to a file
def main():
	#create a list of strings.
	cities = ['Nairobi','', 'Kakamega','', 'Meru','', 'Mombasa']
	#open a file for writing
	outfile = open('cities.txt', 'w')

	#write the list to the file.
	for item in cities:
		outfile.writelines(item + '\n')
		pass
	

	#close the file
	outfile.close()
	pass

	#Open a File for Reading
	open_file_reading()
	print_numbers()

def open_file_reading():
	infile = open('cities.txt', 'r')

	#Read the contents of the file into a list.
	cities = infile.readline()

	#close the file
	infile.close
	#Strip the \n from each element.
	#index = 0
	#while index < len(cities):
	#	cities[index] = cities[index]
	#	index += 1
	
	print cities

#This function saves a list of numbers in an output file
def print_numbers():
	#create a list of numbers
	numbers = [1,2,3,4,5,6,7,7]
	outfile = open('numberlist.txt', 'w')

	for item in numbers:
		outfile.write(str(item) + '\n')
		

	maximum = max(numbers)

	outfile.write(str(maximum) + '\n')

	infile = open('numberlist.txt', 'r')
	numberzx = infile.readlines()
	outfile.close()

	index =0
	while index < len(numberzx):
		numberzx[index] = int(numberzx[index])
		index += 1
		pass

	print numberzx

	

main()