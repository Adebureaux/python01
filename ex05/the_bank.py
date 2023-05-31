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
		if not isinstance(amount, (int, float)) or amount < 0:
			return False
		debtor = None
		creditor = None
		for account in self.accounts:
			if account.name == origin:
				debtor = account
			if account.name == dest:
				creditor = account
			if debtor != None and creditor != None:
				break
		if debtor == None or creditor == None:
			return False
		if not self._is_valid(debtor) or not self._is_valid(creditor):
			print(len(debtor.__dict__))
			print(creditor.__dict__)
			return False
		if debtor == creditor:
			return True
		if debtor.value < amount:
			return False
		debtor.transfer(-amount)
		creditor.transfer(amount)
		return True

	def fix_account(self, name):
		"""Fix account associated to name if corrupted
    @name: str(name) of the account
    @return True if success, False if an error occured"""
		if not isinstance(name, str):
			return False
		recover = None
		for account in self.accounts:
			if account.name == name:
				recover = account.__dict__
				fixed = account
		if recover is None:
			return False
		topop = []
		for attr in recover:
			if attr.startswith('b'):
				topop.append(attr)
		for pop in topop:
			recover.pop(pop)
		if not any(attr.startswith('zip') for attr in recover):
			recover['zip'] = "000-000"
		if not any(attr.startswith('addr') for attr in recover):
			recover['addr'] = "1 rue de la corruption"
		if not 'id' in recover or not isinstance(recover['id'], int):
			recover['id'] = Account.ID_COUNT
			Account.ID_COUNT += 1
		if not 'value' in recover or not isinstance(recover['value'], (int, float)):
			recover['value'] = 0
		if len(recover) % 2 == 0:
			for attr in recover:
				if not attr.startswith('zip') and not attr.startswith('addr') and attr != 'id' and attr != 'value' and attr != 'name':
					recover.pop(attr)
					break
		return self._is_valid(fixed)

	def _is_valid(self, account):
		account_attrs = account.__dict__
		return (
			len(account_attrs) % 2 == 1
			and not any(attr.startswith('b') for attr in account_attrs)
			and any(attr.startswith(('zip', 'addr')) for attr in account_attrs)
			and 'name' in account_attrs
			and 'id' in account_attrs
			and 'value' in account_attrs
			and isinstance(account.name, str)
			and isinstance(account.id, int)
			and isinstance(account.value, (int, float))
		)
