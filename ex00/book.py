from sys import stderr
from datetime import datetime
from recipe import Recipe

class Book:
	
	def __init__(self, name, last_update, creation_date, recipes_list):
		if not isinstance(name, str) or not len(name):
			raise ValueError('name must be a string that contains at least one character.')
		self.name = name

		if not isinstance(last_update, datetime):
			raise TypeError('last_update must be a datetime object.')
		self.last_update = last_update

		if not isinstance(creation_date, datetime):
			raise TypeError('creation_date must be a datetime object.')
		self.creation_date = creation_date

		if not isinstance(recipes_list, dict) or not all(key in ['starter', 'lunch', 'dessert'] for key in recipes_list.keys()):
			raise ValueError("recipes_list must be a dictionary with keys that are either 'starter', 'lunch', or 'dessert'")
		if not all(isinstance(value, Recipe) for value in recipes_list.values()):
			raise TypeError('every value in recipes_list must be an instance of Recipe')
		self.recipes_list = recipes_list

	def get_recipe_by_name(self, name):
		'''Prints a recipe with the name \texttt{name} and returns the instance'''
		# Add code here

	def get_recipes_by_types(self, recipe_type):
		'''Get all recipe names for a given recipe_type'''
		# Add code here 

	def add_recipe(self, recipe):
		'''Add a recipe to the book and update last_update'''
		if not isinstance(recipe, Recipe):
			raise TypeError('recipe must be a Recipe instance')
		self.last_update = datetime.today()
		# Add code here to add the recipe

	def __str__(self):
		'''Return the string to print with the book info'''
		return f"Book information\n" \
					f"=> Name          : {self.name}\n" \
					f"=> Last update   : {self.last_update}\n" \
					f"=> Creation date : {self.creation_date}"

try:
	pancakes = Recipe("Pancakes", 2, 20, ['flour', 'milk', 'eggs'], 'starter', "Classic fluffy pancakes")
	bolognese = Recipe("Spaghetti Bolognese", 3, 45, ['spaghetti', 'ground beef', 'tomatoes'], 'lunch', "Hearty Italian pasta dish")
	cookies = Recipe("Chocolate Chip Cookies", 2, 15, ['flour', 'butter', 'chocolate chips'], 'dessert', "Homemade sweet treats")
	chicken = Recipe("Chicken Stir-Fry", 4, 25, ['chicken breast', 'vegetables', 'soy sauce'], 'lunch', "Quick and flavorful Asian dish")
	smoothie = Recipe("Berry Smoothie", 1, 5, ['berries', 'yogurt', 'honey'], 'dessert', "Refreshing and nutritious drink")

	book = Book("Recettes", datetime.today(), datetime.today(), {'starter': pancakes, 'lunch': bolognese, 'dessert': cookies, 'lunch': chicken})
	print(book.get_recipe_by_name('Pancakes'))
	# book.add_recipe(smoothie)
except (ValueError, TypeError) as e:
	print(f'Invalid book parameters: {e.args[0]}', file=stderr)
