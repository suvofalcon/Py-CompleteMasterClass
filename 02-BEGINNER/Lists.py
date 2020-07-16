"""
Demonstration on Python Lists
"""
# list can be defined as
list1 = []
print(type(list1))

list1 = ['Cisco', 'Juniper', 'Avaya', 10, 10.5, -11]
print(len(list1))  # prints the length of the list

# Access elements in the list using indexes
print(f"First element in the list : {list1[0]}")
print(f"Last element in the list : {list1[-1]}")

# to modify a list element in a specific index
list1[2] = 'HP'
print(list1)

list2 = [-11, 2, 12]
list3 = ['a', 'b', 'c']
print(f"Maximum in the list : {max(list2)}")
print(f"Minimum in the list : {min(list3)}")

# how to add new elements in the list
list1.append(100)
print(list1)

# deleting element from a specific location in the list
del list1[4]
print(list1)
# the second way to remove an element is using pop method
list1.pop(0)
print(list1)
# the third way is to use remove method and specifying the element itself
list1.remove('Juniper')
print(list1)

# to insert an element at a specific location
list1.insert(2, 'Nortel')
print(list1)

# Append one list from another list
list1.extend(list2)
print(list1)

# if the element is present twice, the first index will be returned
print(f"To get the index of a specific element : {list1.index(-11)}")
print(f"To know how many times an element is present in the list : {list1.count(-11)}")

list2 = [-11, 12, 2]
# Sort the list
list2.sort()
print(f"The sorted list : {list2}")
# If we need to reverse the order
list2.reverse()
print(f"The reversed list: {list2}")

# declare another list
list3 = [999, 500, 99, 25, 9, 1]
# Single function for reverse and sorting
print(f"List sorting : {sorted(list3)}")
print(f"List Reverse : {sorted(list3, reverse=True)}")

print(f"To see the help on a function \n :{help(sorted)}")

# List slicing
# follows the same process for string slicing
list4 = [1, 2, 3, 'a', 'b', 'c']
print(list4[0:3])
print(list4[:3])  # will give the same result
print(list4[2:5])
print(list4[2:])
print(list4[:])  # entire list using slicing
print(list4[:-2])  # using negative indexing
print(list4[-4:-1])
print(list4[-3:])