from book import Book
from recipe import Recipe
from datetime import datetime

try:
	pancakes = Recipe("Pancakes", 2, 20, ['flour', 'milk', 'eggs'], 'starter', "Classic fluffy pancakes")
	bolognese = Recipe("Spaghetti Bolognese", 3, 45, ['spaghetti', 'ground beef', 'tomatoes'], 'lunch', "Hearty Italian pasta dish")
	cookies = Recipe("Chocolate Chip Cookies", 2, 15, ['flour', 'butter', 'chocolate chips'], 'dessert', "Homemade sweet treats")
	chicken = Recipe("Chicken Stir-Fry", 4, 25, ['chicken breast', 'vegetables', 'soy sauce'], 'lunch', "Quick and flavorful Asian dish")
	smoothie = Recipe("Berry Smoothie", 1, 5, ['berries', 'yogurt', 'honey'], 'dessert', "Refreshing and nutritious drink")

	book = Book("Recettes", datetime.today(), datetime.today(), {'starter': [pancakes], 'dessert': [cookies], 'lunch': [chicken, bolognese]})
	book.add_recipe(smoothie)
	lunch = book.get_recipes_by_types('lunch')
	for recipe in lunch:
		print(f'{book.get_recipe_by_name(recipe)}\n')
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)