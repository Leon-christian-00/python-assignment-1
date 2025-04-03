# Simple Python Calculator

# Step 1: Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Step 2: Perform the operation based on user input
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Invalid operation. Please enter one of +, -, *, /."

# Step 3: Print the result
print(f"{num1} {operation} {num2} = {result}")