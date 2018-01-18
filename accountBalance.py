class AccountBalance(object):
	"""docstring for AccountBalance"""
	def __init__(self, bal):
		
		self.__balance = bal


	def amount_deposit(self,amount):
		self.__balance += amount
	
	def amount_widthdraw(self, amount):
		if self.__balance >= amount:
			__balance -= amount
		else:
			print "Account Balance: " + self.__balance+" is sufficient to widthdraw: ", amount
	
	def getAccountBalance(self):
		return self.__balance
		
		
		