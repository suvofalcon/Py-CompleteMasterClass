"""
An unordered collection of unique elements - set
"""

# Way to create a set
list_1 = [1, 2, 3, 4, 5, 2, 3]  # list with duplicate elements
# apply the set function on the list_1
print(f"Set out of list - {set(list_1)}")

# We can directly create a set by passing duplicate elements
set1 = set([11, 12, 13, 14, 15, 15, 15, 16, 16, 17, 17, 17])
print(set1)
print(type(set1))

# Find out number of elements in the set
print(f"Number of elements in the set - {len(set1)}")
# Check if an element exists in a set
print(f"Check whether 16 exists in set1 - {16 in set1}")
print(f"Check whether 10 does not exists in set1 - {10 not in set1}")

# Add an element to the set
set1.add(19)
print(f"Check the set1 - {set1}")

# remove an element from set
set1.remove(11)
print(f"Check the set1 - {set1}")

# Some set functions
set2 = {1, 2, 3, 4}
set3 = {3, 5, 8}
print(f"Intersection between two sets - {set2.intersection(set3)}")
print(f"Union between two sets - {set2.union(set3)}")

print(f"Differences between Sets with respect to set2 - {set2.difference(set3)}")
print(f"Differences between Sets with respect to set3 - {set3.difference(set2)}")

# We can use the pop method to remove the first element from a set
print(f"Remove the first element from a set - {set2.pop()}")

# Make the whole set as empty
print(f"Make a whole set clear - {set2.clear()}")

# Frozensets - are immutable sets
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 7])
print(type(fs1))
# we cannot add or remove any element from a frozenset
# However operations like union, intersection and difference is allowed, since they are not attempting to modify
# the contents of the frozenset
