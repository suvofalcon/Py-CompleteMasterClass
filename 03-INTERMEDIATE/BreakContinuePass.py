"""
Break, Continue and Pass
"""
for number in range(10):
    if number == 7:
        break  # It will break out of the for loop completely
    print(number)

list1 = [4, 5, 6]
list2 = [10, 20, 30]
for i in list1:
    for j in list2:
        if j == 20:
            break  # Stops the execution of the inner most for loops
        print(i * j)
    print("Outside the nested loop!!")

# continue
list1 = [4, 5, 6]
list2 = [10, 20, 30]
for i in list1:
    for j in list2:
        if j == 20:
            continue  # ignores the current iteration and goes back for the next
        print(i * j)
    print("Outside the nested loop!!")

# if we want to do nothing
for i in range(10):
    pass
