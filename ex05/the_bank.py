class Account(object):

	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, "value"):
			self.value = 0
		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount


class Bank(object):
	"""The bank"""
	def __init__(self):
		self.accounts = []

	def add(self, new_account):
		"""Add new_account in the Bank
    @new_account: Account() new account to append
    @return True if success, False if an error occured"""
		if not isinstance(new_account, Account):
			return False
		for account in self.accounts:
			if new_account.name == account.name:
				return False
		self.accounts.append(new_account)

	def transfer(self, origin, dest, amount):
		"""Perform the fund transfer
    @origin: str(name) of the first account
    @dest: str(name) of the destination account
    @amount: float(amount) amount to transfer
    @return True if success, False if an error occured"""
		pass

	def fix_account(self, name):
		"""Fix account associated to name if corrupted
    @name: str(name) of the account
    @return True if success, False if an error occured"""
		recover = None
		for account in self.accounts:
			if account.name == name:
				recover = account.__dict__
		if recover is None:
			return False
		
		print(recover)
		return True

	def _is_valid_transaction(self, origin_account, dest_account, amount):
		return amount >= 0 and origin_account.value >= amount

	def _is_valid(self, account):
		account_attrs = account.__dict__
		return (
			len(account_attrs) % 2 == 1
			and not any(attr.startswith('b') for attr in account_attrs)
			and any(attr.startswith('zip') for attr in account_attrs)
			and any(attr.startswith('addr') for attr in account_attrs)
			and 'name' in account_attrs
			and 'id' in account_attrs
			and 'value' in account_attrs
			and isinstance(account.name, str)
			and isinstance(account.id, int)
			and isinstance(account.value, (int, float))
		)

bank = Bank()
account = Account(
	'Smith Jane',
	zip='911-745',
	addr='abc',
	value=1000.0,
	ref='1044618427ff2782f0bbece0abd05f31')
bank.add(account)

print(bank._is_valid(account))
print(bank.fix_account("Smith Jane"))
