from sys import stderr
from datetime import datetime
from recipe import Recipe

class Book:
	
	def __init__(self, name, recipes_list={}):
		if not isinstance(name, str) or not len(name):
			raise ValueError('Book __init__ Book name must be a string that contains at least one character.')
		self.name = name

		if not isinstance(recipes_list, dict):
			raise TypeError('__init__ recipes_list must be a dictionary.')
		if len(recipes_list):
			if not all(key in ['starter', 'lunch', 'dessert'] for key in recipes_list.keys()):
				raise ValueError("Book __init__ recipes_list keys must be either 'starter', 'lunch', or 'dessert'.")
			if not all(isinstance(value, list) and all(isinstance(recipe, Recipe) for recipe in value) for value in recipes_list.values()):
				raise TypeError('Book __init__ every value in recipes_list must be a list of instances of Recipe.')
		self.recipes_list = recipes_list
		self.creation_date = datetime.today()
		self.last_update = self.creation_date

	def get_recipe_by_name(self, name):
		'''Prints a recipe with the name \texttt{name} and returns the instance'''
		for recipes in self.recipes_list.values():
				for recipe in recipes:
						if recipe.name == name:
								print(recipe)
								return recipe
		print("Recipe not found.")
		return None

	def get_recipes_by_types(self, recipe_type):
		'''Get all recipe names for a given recipe_type'''
		if not recipe_type in ['starter', 'lunch', 'dessert']:
			raise ValueError("Book get_recipes_by_types() argument recipe_type must be a string which can be 'starter', 'lunch' or 'dessert'.")
		return [recipe.name for recipes in self.recipes_list.values() for recipe in recipes if recipe.recipe_type == recipe_type]

	def add_recipe(self, recipe):
		'''Add a recipe to the book and update last_update'''
		if not isinstance(recipe, Recipe):
			raise TypeError('Book add_recipe() argument recipe must be a Recipe instance.')
		self.last_update = datetime.today()
		recipe_list = self.recipes_list.get(recipe.recipe_type, [])
		recipe_list.append(recipe)
		self.recipes_list[recipe.recipe_type] = recipe_list

	def __str__(self):
		'''Return the string to print with the book info'''
		return f"Book information\n" \
					f"=> Name          : {self.name}\n" \
					f"=> Last update   : {self.last_update}\n" \
					f"=> Creation date : {self.creation_date}"
