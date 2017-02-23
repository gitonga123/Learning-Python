#This program calculates the gross pat for
# each of wegan's baristas.

#NUM_EXPENSES is used as a constant for the
# size of the list


def main():
	NUM_EMPLOYEES = (input("Enter the number of Employees "))
	#create a list to hold employee hours.
	hours = [0] * NUM_EMPLOYEES
	#Get each employee's hours worked.
	for index in range(NUM_EMPLOYEES):
		print "Enter the hours worked by employee ", index+1, ':'
		hours[index] = float(input())
		pass
	#Get the hourly pay rate.
	pay_rate = float(input("Enter the hourly pay rate: "))
	#Get each employee's hours worked.

	#Display each employee's gross pay.
	
	for index in range(NUM_EMPLOYEES):
		gross_pay = hours[index] * pay_rate
		print "Gross pay for employee ", index+1, "=" , gross_pay
		pass
	pass

main()