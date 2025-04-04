# Simple Python Calculator

# Step 1: Take input from the user
a = int(input("enter your first number:"))
b = int(input("enter your second number:"))
op = input("choose your operation : + , - , / , * :")

# Step 2: Perform the operation based on user input & Print the result
if op == "+":
    res = int(a + b)
    print(f"the result of: {a} {op} {b} = {res}")
elif op == "-":
    res = int(a - b)
    print(f"the result of: {a} {op} {b} = {res}")
elif op == "*":
    res = int(a * b)
    print(f"the result of: {a} {op} {b} = {res}")
elif op == "/":
    res = int(a // b)
    print(f"the result of: {a} {op} {b} = {res}")
else:
    print(f"wrong operation")
