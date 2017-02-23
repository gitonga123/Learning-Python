from __future__ import print_function

ot_multiplier = 1.5
base_hours = 40

hours =float(input("Enter the number of hours worked "))
pay_rate = float(input("Enter your hourly pay rate "))

if hours > base_hours:
	overtime = hours - base_hours

	bonus = overtime * ot_multiplier

	salary = bonus + (base_hours * pay_rate)
	pass
else:
	salary = pay_rate * hours


print("Your total Gross Pay is $",format(salary,(',.2f')), sep='')
