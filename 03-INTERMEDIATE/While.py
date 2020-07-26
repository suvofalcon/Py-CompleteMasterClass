"""
While loops
Execute a code as long as the condition is true
"""
x = 1

while x <= 10:  # statements will keep on getting executed until the condition in while becomes False
    print(x)
    x = x + 1

while x <= 10:
    print(x)
    x = x + 1
else:
    print("x is now greater than 10")  # this gets executed when the condition in while becomes False
