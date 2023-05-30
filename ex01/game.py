class GotCharacter:
	def __init__(self, first_name, is_alive=True):
		self.first_name = first_name
		self.is_alive = is_alive

class Stark(GotCharacter):
	'''A class representing the Stark family. Or when bad things happen to good people.'''
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is comming"
	def print_house_words(self):
		print(self.house_words)
	def die(self):
		self.is_alive = False

class Targaryen(GotCharacter):
	'''A class representing the Targaryen family. Or when 3 dragons in not enough'''
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Targaryen"
		self.house_words = "Fire and Blood"
	def print_house_words(self): 
		print(self.house_words)
	def die(self):
		self.is_alive = False

if __name__ == "__main__":
	arya = Stark("Arya")
	arya.print_house_words()
	print(arya.is_alive)
	print(arya.__dict__)
	print(arya.__doc__)

	daenerys = Targaryen("Daenerys")
	daenerys.print_house_words()
	print(daenerys.is_alive)
	daenerys.die()
	print(daenerys.__dict__)
	print(daenerys.__doc__)