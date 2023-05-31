from book import Book
from recipe import Recipe
from datetime import datetime
from sys import stderr
from time import sleep

# Tests that should not raise an exception:
try:
	# Create some recipes
	pancakes = Recipe("Pancakes", 2, 20, ['flour', 'milk', 'eggs'], "Classic fluffy pancakes", 'starter')
	bolognese = Recipe("Spaghetti Bolognese", 3, 45, ['spaghetti', 'ground beef', 'tomatoes'], "Hearty Italian pasta dish", 'lunch')
	cookies = Recipe("Chocolate Chip Cookies", 2, 15, ['flour', 'butter', 'chocolate chips'], "Homemade sweet treats", 'dessert')
	chicken = Recipe("Chicken Stir-Fry", 4, 25, ['chicken breast', 'vegetables', 'soy sauce'], "Quick and flavorful Asian dish", 'lunch')
	smoothie = Recipe("Berry Smoothie", 1, 5, ['berries', 'yogurt', 'honey'], "Refreshing and nutritious drink", 'dessert')

	# Create a book and add recipes
	book = Book("Recettes", {'starter': [pancakes], 'lunch': [bolognese, chicken], 'dessert': [cookies, smoothie]})

	# Test get_recipe_by_name
	recipe = book.get_recipe_by_name("Chicken Stir-Fry")

	recipe = book.get_recipe_by_name("Salad")  # Recipe not found
	print(recipe)  # Should print None

	# Test get_recipes_by_types
	recipes = book.get_recipes_by_types("dessert")
	print(recipes)  # Should print a list of dessert recipe names

	recipes = book.get_recipes_by_types("lunch")
	print(recipes)  # Should print a list of lunch recipe names

	# Test add_recipe
	new_recipe = Recipe("Salad", 1, 10, ['lettuce', 'tomatoes', 'cucumber'], "Fresh and healthy salad", 'starter')
	book.add_recipe(new_recipe)

	recipes = book.get_recipes_by_types("starter")
	print(recipes)  # Should print a list of starter recipe names including "Salad"

	# Test last_update
	before_update = book.last_update
	new_recipe = Recipe("Pasta", 1, 20, ['pasta', 'sauce'], "Sample description", 'lunch')
	book.add_recipe(new_recipe)
	print(str(book))
	if before_update == book.last_update:  # before_update should not be equal last_update
		print('Error ! add_recipe() does not update last_update')

except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)


# Tests that should raise an exception:
try:
	recipes = book.get_recipes_by_types("breakfast")  # Invalid recipe type
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	new_recipe = Recipe("Salad", 1, 10, ['lettuce', 'tomatoes', 'cucumber'], "Fresh and healthy salad", 'breakfast')  # Invalid recipe type
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	new_recipe = Recipe("Salad", 1, 10, ['lettuce', 'tomatoes', 'cucumber'], "Fresh and healthy salad", 5)  # Invalid recipe type
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	new_recipe = Recipe("Salad", 1, 10, ['lettuce', 'tomatoes', 'cucumber'], 5, 'starter')  # Invalid description
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	new_recipe = Recipe("Pasta", -1, 20, ['pasta', 'sauce'], "Sample description", 'lunch')  # Negative cooking time
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	new_recipe = Recipe("Soup", 3, 25, 'ingredient', "Sample description", 'starter')  # Invalid ingredients (not a list)
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	new_recipe = Recipe("Salad", 2, 15, ['lettuce', 'tomatoes', 5], "Sample description", 'lunch')  # Invalid ingredient (not a string)
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	book = Book("Recettes", {'starter': pancakes})  # Invalid recipe_list dict value (not a list)
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	book = Book("Recettes", ['starter', pancakes])  # Invalid recipe_list (not a dict)
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)