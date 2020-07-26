"""
Dictionaries - key value pair
Indexed by Keys, they are also mutable
"""

dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}
print(dict1)

# Extract the corresponding value for specific key
print(dict1["IOS"])
# Adding new entry to the dictionary
dict1["RAM"] = "128"
print(dict1)
# Update a value for a particular key
dict1["IOS"] = "12.3"
print(dict1)
# delete  a pair from the dictionary
del dict1["Ports"]
print(dict1)
# length of the dictionary - number of key value pairs inside a dictionary
print(len(dict1))

# to check whether a particular key exists in the dictionary
print(f"Check whether this key exists in the dictionary - {'IOS' in dict1}")

# to get a list having the keys in the dictionary as elements
print(dict1.keys())
# to get a list having the values in the dictionary as elements
print(dict1.values())

# to get a tuple from dictionary, where each item in the tuple is a key-value pair
print(dict1.items())

# Order of elements in Keys, values and items will be consistent with the order in which the dictionary was created

# however we can get a sorted list of values in the following manner
my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}
print(f"First element after sorting the values - {sorted(my_dict.values())[0]}")
print(type(sorted(my_dict.values())))  # returns a list

# Conversions between data types
num = 2
f = 2.5
# converting integers and floating point to string
num2 = str(num)
f2 = str(f)

# Now we will do it backwards
str1 = "5"
num3 = int(str1)
print(type(num3))

str2 = "5.5"
num4 = float(str2)
print(type(num4))

# Convert tuple to list and set
print(f"List conversion - {list((1, 2, 3))}")
print(f"Set conversion - {set((1, 2, 3))}")
print(f"Tuple conversion from a list - {tuple([4, 5, 6])}")

# Convert integer to binary and hex
print(f"Convert integer 10 to binary - {bin(10)}")
print(f"Convert integer 19 to hex - {hex(19)}")

# Conversion of a  binary to integer
num = 25
bin_num = bin(num)
hex_num = hex(num)
print(f"Converting back to integer from binary - {int(bin_num, 2)}")
print(f"Converting back to integer from hex - {int(hex_num, 16)}")
