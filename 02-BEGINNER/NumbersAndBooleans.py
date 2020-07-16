"""
Demonstration of Numbers and Booleans in Python
"""
# Lets define an integer and a floating point number
num1 = 10
num2 = 3.5
print(type(num1))
print(type(num2))

print(f"Adding both the numbers : {num1+num2}")
print(f"Dividing two numbers : {num1/num2}")
print(f"Integer division of two numbers : {num1//num2}")
print(f"Modulo of two numbers : {num1 % num2}")

# Comparison operator
print(f"Comparison : {num1 > num2}")
print(f"Comparison : {num1 == num2}")

# Conversion
print(f"Conversion of float to integer : {int(num2)}")
print(f"Conversion of integer to float : {float(num1)}")

print(f"Absolute of a negative number  {abs(-10)}")
print(f"Maximum of two numbers :{max(num1, num2)}")
print(f"Power Function : {pow(num1, num2)}")

print(f"String comparison is case sensitive, for example python and Python is : {'python' == 'Python'}")

# Boolean comparisons
print(f"And comparison : {1==1 and 2==2}")
print(f"And comparison : {1==1 and 2==3}")
print(f"Or Comparison : {1--1 and 2==3}")

