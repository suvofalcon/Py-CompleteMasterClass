"""
If, Elif and Else
"""
x = 100
if x > 5:
    print("x is greater than 5")
    print(x * 2)
elif x == 5:
    print("x is 5")
else:
    print("x is smaller")

if x == 5 and type(x) is int:
    print("x equals 5 and x is an integer")
    print(x)
elif x == 10 and type(x) is int:
    print("x is an integer but not equals 5")
else:
    print("x is not matching any conditions")

# else statement is optional and so is elif...
