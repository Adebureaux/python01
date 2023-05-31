from sys import stderr

class Recipe:

	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		if not isinstance(name, str) or not len(name):
				raise ValueError('Recipe __init__ name must be a string that contains at least one character.')
		self.name = name

		if not isinstance(cooking_lvl, int) or cooking_lvl < 1 or cooking_lvl > 5:
			raise ValueError('Recipe __init__ cooking_lvl must be an integer that is between 1 and 5.')
		self.cooking_lvl = cooking_lvl

		if not isinstance(cooking_time, int) or cooking_time < 0:
			raise ValueError('Recipe __init__ cooking_time must be a positive integer')
		self.cooking_time = cooking_time

		if not isinstance(ingredients, list) or not len(ingredients) or not all(isinstance(item, str) for item in ingredients):
			raise TypeError('Recipe __init__ ingredients must be a list that contains only strings (at least one).')
		self.ingredients = ingredients

		if not isinstance(description, str):
			raise TypeError('Recipe __init__ description must be a string')
		self.description = description

		if recipe_type not in ['starter', 'lunch', 'dessert']:
			raise ValueError("Recipe __init__ recipe_type must be a string which can be 'starter', 'lunch' or 'dessert'.")
		self.recipe_type = recipe_type


	def __str__(self):
		'''Return the string to print with the recipe info'''
		txt = f'''Recipe information
=> Name          : {self.name}
=> Cooking level : {self.cooking_lvl}
=> Cooking time  : {self.cooking_time} minutes
=> Ingredients   : {self.ingredients}
=> Recipe type   : {self.recipe_type}'''
		if len(self.description):
				txt += f'\n\
=> Description   : {self.description}'
		return txt