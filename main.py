"""
You will be given a data structure containing information on different recpies. It will be a list of tuples, where each tuple represents a single recipe. The tuple will have three elements in this order: the name of the recipe, the name of the chef who created it, and a tuple of ingredients.
For example:
[
  ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
  ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
  ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
  ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
  ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
  ("Latkes", "Hallie", ("Potato", "Oil")),
  ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]
We are interested in which chefs use the greatest variety of ingedients across all of their recipes. For example, Xinting uses the following ingredients (in alphabetical order):
['Beef', 'Carrot', 'Chicken Stock', 'Onion', 'Peas', 'Tomato']
This is a larger number of ingredients than any other chef uses. Thus, we will say that Xinting is the most varied chef.
Write a function that takes in a recipes data structure and returns the top two most varied chefs, along with an alphabetically sorted list of the ingredients they each use. This output must be a list of tuples. Each tuple will have two elements in this order: the name of the chef, and a sorted list of the unique ingredients they use.
Examples:
recipes_1 = [
  ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
  ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
  ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
  ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
  ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
  ("Latkes", "Hallie", ("Potato", "Oil")),
  ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]
most_varied(recipes_1) => [
  ('Xinting', ['Beef', 'Carrot', 'Chicken Stock', 'Onion', 'Peas', 'Tomato']), 
  ('Amy', ['Cheese', 'Chicken Cream', 'Pepper', 'Tater tots'])
]
recipes_2 = [
  ("Latkes", "Hallie", ("Potato", "Oil")),
  ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
]
most_varied(recipes_2) => [('Sam', ['Beef', 'Cheese', 'Tortilla']), ('Hallie', ['Oil', 'Potato'])]
"""

def most_varied(recipes):
  hashtable = {}
  for recipe in recipes:
    if recipe[1] not in hashtable:
      hashtable[recipe[1]] = set(recipe[2])    
    else:
      for i in range(len(recipe[2])):
        hashtable[recipe[1]].add(recipe[2][i])
  print (hashtable)
  maxLen = []
  output = []
  for key,value in hashtable.items():
    output.append((key, list(sorted(value))))
    maxLen.append(len(value))
  X=[x for _, x in sorted(zip(maxLen, output),reverse=True)]
  print(X)

  return X[:2]
  
recipes_1 = [
  ("Burrito", "Sam", ("Beef", "Cheese", "Tortilla")),
  ("Hot Dish", "Amy", ("Tater tots", "Chicken Cream", "Cheese", "Pepper")),
  ("Stew", "Xinting", ("Beef", "Onion", "Tomato", "Carrot")),
  ("Taco", "Sam", ("Tortilla", "Cheese", "Beef")),
  ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
  ("Latkes", "Hallie", ("Potato", "Oil")),
  ("Pea Soup", "Xinting", ("Peas", "Onion", "Carrot", "Chicken Stock")),
]
assert most_varied(recipes_1) == [
  ('Xinting', ['Beef', 'Carrot', 'Chicken Stock', 'Onion', 'Peas', 'Tomato']), 
  ('Amy', ['Cheese', 'Chicken Cream', 'Pepper', 'Tater tots'])
]

recipes_2 = [
  ("Latkes", "Hallie", ("Potato", "Oil")),
  ("Chalupa", "Sam", ("Tortilla", "Beef", "Cheese")),
]
assert most_varied(recipes_2) == [
  ('Sam', ['Beef', 'Cheese', 'Tortilla']),
  ('Hallie', ['Oil', 'Potato'])
]

print("All test cases passed!")
print("Finished early? Discuss time & space complexity.")