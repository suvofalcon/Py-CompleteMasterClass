"""
Ranges in python
"""
print(f"Range of 10 - {list(range(10))}")
print(f"Range of 10 - {list(range(5, 10))}")  # start from 5 and go upto but not including 10
print(f"Range of 10 - {range(0, 10, 2)}")  # even numbers between 0 and 10

rng = list(range(0, 10, 2))
print(f"Check whether 2 is there in the rng - {2 in rng}")

# In python 3 range gets it own data types and since we are converting a range object to list, we can thereafter
# use all list functions

# to print out the index of a specific value
r1 = range(10, 100, 10)
print(r1.index(30))
