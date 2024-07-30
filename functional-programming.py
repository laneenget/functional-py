from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(lambda x: x.capitalize(), my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort
# the numbers from lowest to highest
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
print(list(zip(my_strings, my_numbers)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
over50 = filter(lambda x: x > 50, scores)
print(list(over50))

# 4 Combine all of the numbers that are in a list on
# this file using reduce (my_numbers and scores). What
# is the total?
def add(x, y):
    return x+y

sum_my_numbers = reduce(add, my_numbers)
sum_scores = reduce(add, scores)
print(sum_my_numbers + sum_scores)