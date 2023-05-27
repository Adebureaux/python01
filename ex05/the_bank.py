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
		# test if new_account is an Account() instance and if
		# it can be appended to the attribute accounts
		# ... Your code ...
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
		pass

	def _is_valid_account(self, account):
		account_attrs = dir(account)
		return (
			len(account_attrs) % 2 == 1
			and not any(attr.startswith('b') for attr in account_attrs)
			and not any(attr.startswith(('zip', 'addr')) for attr in account_attrs)
			and 'name' in account_attrs
			and 'id' in account_attrs
			and 'value' in account_attrs
			and isinstance(account.name, str)
			and isinstance(account.id, int)
			and isinstance(account.value, (int, float))
	)

	def _is_valid_transaction(self, origin_account, dest_account, amount):
		return amount >= 0 and origin_account.value >= amount

	def _is_corrupted_account(self, account):
		account_attrs = dir(account)
		return (
			len(account_attrs) % 2 == 0
			or any(attr.startswith('b') for attr in account_attrs)
			or any(attr.startswith(('zip', 'addr')) for attr in account_attrs)
			or 'name' not in account_attrs
			or 'id' not in account_attrs
			or 'value' not in account_attrs
			or not isinstance(account.name, str)
			or not isinstance(account.id, int)
			or not isinstance(account.value, (int, float))
		)