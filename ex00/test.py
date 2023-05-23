from book import Book
from recipe import Recipe
from datetime import datetime
from sys import stderr
from time import sleep

# Tests that should not raise an exception:
try:
	# Create some recipes
	pancakes = Recipe("Pancakes", 2, 20, ['flour', 'milk', 'eggs'], 'starter', "Classic fluffy pancakes")
	bolognese = Recipe("Spaghetti Bolognese", 3, 45, ['spaghetti', 'ground beef', 'tomatoes'], 'lunch', "Hearty Italian pasta dish")
	cookies = Recipe("Chocolate Chip Cookies", 2, 15, ['flour', 'butter', 'chocolate chips'], 'dessert', "Homemade sweet treats")
	chicken = Recipe("Chicken Stir-Fry", 4, 25, ['chicken breast', 'vegetables', 'soy sauce'], 'lunch', "Quick and flavorful Asian dish")
	smoothie = Recipe("Berry Smoothie", 1, 5, ['berries', 'yogurt', 'honey'], 'dessert', "Refreshing and nutritious drink")

	# Create a book and add recipes
	book = Book("Recettes", datetime.today(), datetime.today(), {'starter': [pancakes], 'lunch': [bolognese, chicken], 'dessert': [cookies, smoothie]})

	# Test get_recipe_by_name
	recipe = book.get_recipe_by_name("Chicken Stir-Fry")
	print(recipe)  # Should print the recipe details

	recipe = book.get_recipe_by_name("Salad")  # Recipe not found
	print(recipe)  # Should print None

	# Test get_recipes_by_types
	recipes = book.get_recipes_by_types("dessert")
	print(recipes)  # Should print a list of dessert recipe names

	recipes = book.get_recipes_by_types("lunch")
	print(recipes)  # Should print a list of lunch recipe names

	# Test add_recipe
	new_recipe = Recipe("Salad", 1, 10, ['lettuce', 'tomatoes', 'cucumber'], 'starter', "Fresh and healthy salad")
	book.add_recipe(new_recipe)

	recipes = book.get_recipes_by_types("starter")
	print(recipes)  # Should print a list of starter recipe names including "Salad"

	# Test last_update
	before_update = book.last_update
	new_recipe = Recipe("Pasta", 1, 20, ['pasta', 'sauce'], 'lunch', "Sample description")
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
	new_recipe = Recipe("Salad", 1, 10, ['lettuce', 'tomatoes', 'cucumber'], 'breakfast', "Fresh and healthy salad")  # Invalid recipe type
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	new_recipe = Recipe("Salad", 1, 10, ['lettuce', 'tomatoes', 'cucumber'], 5, "Fresh and healthy salad")  # Invalid recipe type
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	new_recipe = Recipe("Salad", 1, 10, ['lettuce', 'tomatoes', 'cucumber'], 'starter', 5)  # Invalid description
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	new_recipe = Recipe("Pasta", -1, 20, ['pasta', 'sauce'], 'lunch', "Sample description")  # Negative cooking time
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	new_recipe = Recipe("Soup", 3, 25, 'ingredient', 'starter', "Sample description")  # Invalid ingredients (not a list)
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	new_recipe = Recipe("Salad", 2, 15, ['lettuce', 'tomatoes', 5], 'lunch', "Sample description")  # Invalid ingredient (not a string)
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	book = Book("Recettes", datetime.today(), datetime.today(), {'starter': pancakes})  # Invalid recipe_list dict value (not a list)
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)

try:
	book = Book("Recettes", datetime.today(), datetime.today(), ['starter', pancakes])  # Invalid recipe_list (not a dict)
except (ValueError, TypeError) as e:
	print(f'Invalid parameter: {e.args[0]}', file=stderr)