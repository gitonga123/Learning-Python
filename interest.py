#This program demonstrates keyword arguments.
def main():
	#show the amount of simple interest, using 0.01
	# interest rate per period, 10 as the number of perios and 
	# $10,000 as the orincipal.
	show_interest(rate=0.01, periods =10, principal = 10000.0)
	# The show_interest function displays the amount
	# of the simple interest for a given principal, interest rate
	# per period, and number of periods

	
def show_interest(principal, rate, periods):
	interest = principal * rate * periods
	print "The simple interest will be $",  interest
	
main()