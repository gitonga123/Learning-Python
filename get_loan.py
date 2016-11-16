from __future__ import print_function

salary_yearly = 30000
number_of_years = 2

salary = int(input("Enter the amount of cash earned yearly "))
years = int(input("Enter the number of years worked "))

if salary >= salary_yearly:
	if years >= number_of_years:
		print("Loan Application Accepted. Contact the Bank Manager for more information")
		
	else:
		print("The number of year(s) " ,years," worked is less the number of years required ", number_of_years)

else:
	print("Your salary earned Yearly ",salary ," is less than the mimimum threshold ", salary_yearly)