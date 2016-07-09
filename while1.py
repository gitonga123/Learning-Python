keep_going = 'y'

while keep_going == 'y':
	sales = float(input('Enter the amount of sales: '))

	comm_rate = float(input('Enter the commission rate: '))

	commission = sales * comm_rate
	

	print 'The Commission is $', format(commission)

	keep_going = input ('Do you want to calculate another commission(Enter Y fo yes): ')