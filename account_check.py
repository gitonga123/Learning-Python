import accountBalance

def main():

	print "Welcome to Equity Trial Bank Account"

	start_balance = 5000.55

	print "Your starting balance is: ", start_balance

	print "Kidding, i know you are rich enter your own balance if you don't mind;"

	start_balance = (float(input("Enter your preferred starting balance ?")))

	accounts = accountBalance.AccountBalance(start_balance)

	print "Your balance is ", start_balance
	deposit = (float(input("Please enter the amount to deposit to account")))

	accounts.amount_deposit(deposit)

	print "Your balance after the deposit is: ",accounts.getAccountBalance()

	width = (float(input("Please enter the amount of money to widthdraw?")))

	accounts.amount_widthdraw(width)

	print "Your Current balance after: " + width + " widthdraw is: " + accounts.getAccountBalance()


main()