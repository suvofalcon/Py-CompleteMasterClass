"""
Nested loops - examples
"""

X = 'Cisco'
if 'i' in X:
    if len(X) > 3:
        print(X, len(X))

# The below code is same as above
if 'i' in X and len(X) > 3:
    print(X, len(X))

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        print(i * j)
    print(f"For loop element completed - {i}")

x = 1
while x <= 10:
    z = 5
    x += 1
    while z <= 10:
        print(z)
        z += 1

for number in range(10):
    if 5 <= number <= 9:
        print(number)