"""
Demonstration of Python Strings
Sequence of characters including letters, numbers and even other symbols
"""
# create a string
my_string = 'this is my first string'  # we can use both single quote and double quote
print(my_string)
# Triple quote can be used to enter strings in new line (\ is used for escaping new line characters)
my_string = '''This is \
my second \
string with triple \
quote'''
print(my_string)

string1 = 'Cisco Router'
print(string1[0])
print(f"To check the last character and second last character : {string1[-1]} and {string1[-2]}")
print(f"The length of the string : {len(string1)}")

# index with the first occurrence of the character
string2 = 'Cisco Switch'
print(string2.index('i'))  # i occurs twice and returns the index of the first occurrence
print(f"The number of times 'i' has occurred in the string is {string2.count('i')}")

"""
String Methods
"""

# if we need to find a substring, we can have the result return the first index of the substring
print(string2.find('sco'))  # If the substring is not found, find method returns -1
print(f"Convert our string to lower and upper : {string2.lower()} and {string2.upper()}")

# To check whether our string starts with the specific character as the first character or ends with the
# specific character
print(string2.startswith('C'))
print(string2.endswith('r'))

# Method to eliminate all white spaces  in the beginning and end of the string
print(string2.strip())

# to remove leading and trailing characters
string2 = '$$$$$Cisco Switch$$$$$'
print(f"Stripping leading and trailing characters : {string2.strip('$')}")
# String replace method can be used as
print(string2.replace(" ", ""))

# Extract strings based on delimiters
string3 = 'Cisco, Juniper, HP, Avaya, Nortel'
print(string3.split(", "))

# In case we need to insert individual characters between each of the character of the string
print("_".join(string2))

# we can concatenate two strings
print("Cisco" + " Switch")
print("Cisco" * 3)

# If we need to check whether a character is a part of the string
print("o" in string2)
print("b" not in string2)

"""
String formatting
"""

# "Cisco model: 2600XM, 2 WAN Slots, IOS 13.5"
# Using String formatting the above can be written as
print("Cisco model: %s, %d WAN Slots, IOS %f" % ("2600XM", 2, 13.5))
print("Cisco model: %s, %d WAN Slots, IOS %.2f" % ("2600XM", 2, 13.5))
# This can also be done as
print("Cisco model: {}, {} WAN Slots, IOS {}".format("2600XM", 2, 13.5))
print("Cisco model: {0}, {1} WAN Slots, IOS {2}".format("2600XM", 2, 13.5))

"""
String Slices
"""
# Slicing will begin from the start index, will go upto but not include the second index
string5 = 'O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2'
print(string5[5: 15])
# to start from beginning
print(string5[:15])
# to slice everything
print(string5[:])
# using negative indexes also we can slice
print(string5[-9: -1])
# from beginning till end (omitting the last five characters)
print(string5[: -5])
# We want to extract alternate characters - this is called using a step
# The format is string[start: stop: step] - All three start, stop and step are optional
print(string5[::2])
# to print a string easily in reverse order
print(string5[::-1])

string6 = '0123456789'
print(f"All even numbers using step slicing of string {string6[::2]}")
print(f"All odd numbers using step slicing of string {string6[1::2]}")
print(f"All odd numbers using step slicing of string less than 7 - {string6[1:7:2]}")
