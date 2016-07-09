#This program calculates the gross pat for
# each of wegan's baristas.

#NUM_EXPENSES is used as a cosntant for the
# size of the list
NUM_EMPLOYEES = 6

def main():
	#create a list to hold employee hours.
	hours = [0]* NUM_EMPLOYEES
	pay_rate = float(input("Enter the hourly pay rate: "))
	#Get each employee's hours worked.
	for index in range(NUM_EMPLOYEES):
		gross_pay = hours[index] * pay_rate
		print ("Gross pay for employee ", index+1, gross_pay)
		pass
	pass

main()