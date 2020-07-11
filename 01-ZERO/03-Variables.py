# declare a variable

a = 10

# now in order to print the location identifier of the variable in the memory, we use the inbuilt default function
# of python as id
print(id(a))
print(id(10))
# both the above values will be same, because a will point to the same location in memory which has the value 10
b = a
print(id(b))  # Now b also points to the same location, hence will have the same location identifier
b = 20
print(id(b))  # now the identifier will change, because it is pointing to a different value in the memory
