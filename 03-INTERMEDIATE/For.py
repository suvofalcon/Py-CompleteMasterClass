"""
For loops in Python
"""
# define a list
vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

# iterator
for each_vendor in vendors:
    print(each_vendor)

my_string = "Cisco"
for letter in my_string:
    print(letter)
    print(letter * 2)
    print(letter * 3)

for i in range(10):
    print(i * 2)

# We wil print each element of vendors by its index
for element_index in range(len(vendors)):
    print(vendors[element_index])

# If we want to print the index and the element in that index, we can do that using enumerate function in python
for element_index, element in enumerate(vendors):
    print(element_index, element)

# If we want to execute a code after the for loop has completely finished executing
for element in vendors:
    print(element)
else:
    print("The end of list has been reached")