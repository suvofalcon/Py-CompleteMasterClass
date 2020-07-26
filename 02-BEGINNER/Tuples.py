"""
Tuples are immutable lists
Ordered collection of non-unique elements - indexes and duplicates are allowed
"""
my_tuple = ()
# in order to create a single element in a tuple, we need to give a 'comma' otherwise it wont be regarded as a tuple
my_tuple = (9, )
print(type(my_tuple))
# tuple supports indexing like strings and lists
my_tuple = (1, 2, 3, 4, 5)
print(f"First element of the tuple - {my_tuple[0]}")
print(f"Last element of the tuple - {my_tuple[-1]}")

# Since tuples are immutable, we cannot add or remove element in a tuple

# We can define a tuple of variables and assign it to a tuple of values
tuple1 = ("Cisco", "2600", "12.4")
(vendor, model, iOS) = tuple1
# Now we will print out the variables, which will print out the corresponding values assigned from the tuple
# This is also called tuple packing and unpacking
# Both tuples should have the same number of elements
print(f"Values of the variables - {vendor}, {model}, {iOS}")
# We can do the above in a single statement
(a, b , c) = (10, 20, 30)
print(f"Values of the variables - {a}, {b}, {c}")
print(f"To see a method available for a tuple : {dir(tuple1)}")

# Tuples are immutable whereas lists are mutable
# Tuples have a fixed length and lists have variable length
# tuples we have parenthesis, whereas lists have square brackets
# tuples have less available methods and operations than lists

# Tuple methods
tuple2 = (1, 2, 3, 4)
print(f"Length of the tuple - {len(tuple2)}")
print(f"Lowest and max value in a tuple - {min(tuple2)} and {max(tuple2)}")
# tuple concatenation
tuple3 = tuple2 + (5, 6, 7)
print(f"Concatenated tuple - {tuple3}")
print(f"Multiplication operation on a tuple - {tuple2 * 2}")
# slicing is also possible in tuple - exactly same as lists
print(tuple2[0: 2])  # will return a tuple
# Check whether an element exists in a tuple
print(f"Whether 8 exists in the tuple - {8 in tuple2}")

my_tuple[0]  # returns the first element in the tuple (index 0)
my_tuple[-1]  # returns the last element in the tuple (index -1)
my_tuple[0:2]  # returns (1, 2)
my_tuple[:2]  # returns (1, 2)
my_tuple[1:]  # returns (2, 3, 4)
my_tuple[:]  # returns (1, 2, 3, 4)
my_tuple[:-2]  # returns (1, 2) - will return the last two elements of the tuple
my_tuple[-2:]  # returns (3, 4)
my_tuple[::-1]  # returns (4, 3, 2, 1)
my_tuple[::2]  # returns (1, 3)

# to delete a complete tuple
del tuple2

