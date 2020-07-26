"""
Exceptions in python 3
"""
for index in range(5):
    try:
        print(index/1)
    except ZeroDivisionError as e:
        print(e, "Division by zero is not allowed")
    print("rest of the code!!")

# We can have multiple except clauses
for index in range(5):
    try:
        print(index/1)
    except ZeroDivisionError:
        print("Zero division error")
    except NameError:
        print("Name Error detected")
    except ValueError:
        print("Wrong Value")

# Else can be used and it will be executed if the code raises no exception
try:
    print(4 /2)
except NameError:
    print("Name Error!!")
else:
    print("No Exceptions were raised")
finally:
    print("This code gets executed regardless of whatever happens")

# How finally gets executed even in exception situation
for index in range(5):
    try:
        print(index/0)
    except ZeroDivisionError as e:
        print(e, "Division by zero is not allowed")
    else:
        print("No Exception has happened!!")
    finally:
        print("rest of the code!!")
