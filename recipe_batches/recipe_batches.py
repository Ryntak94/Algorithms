#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    keys = recipe.keys()
    max_recipe = 1000
    for i in keys:
        if max_recipe and i in ingredients:
            max_recipe = math.floor(min(ingredients[i]/recipe[i], max_recipe))
        elif i in ingredients:
            max_recipe = math.floor(ingredients[i]/recipe[i])
        else:
            max_recipe = 0
    return max_recipe


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
