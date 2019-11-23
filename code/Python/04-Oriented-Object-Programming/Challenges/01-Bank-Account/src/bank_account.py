class Account():
	'''
	Model a bank account
	'''
	def __init__(self, name_holder, account_number, current_balance = 2000):
		self.name_holder = name_holder
		self.account_number = account_number
		self.current_balance = current_balance


	def withdraw_money(self, balance):
		balance_account = self.current_balance - balance
		return self.current_balance

	def deposit_money(self, balance):

		balance_account = self.current_balance + balance
		return balance_account

	def dump(self):
		return  self.name_holder, self.account_number, self.current_balance
		

ross_account = Account("Ross", 9502018482, 1350)
print(ross_account.dump())
#print(ross_account.deposit_money(200))
rachel_account = Account("Rachel", 1945729572, 3450)
