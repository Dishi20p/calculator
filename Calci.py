# user to enter two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# user to choose an operation
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed"


operation = float(input("Enter your choice: "))

if operation == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operation == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input. Please enter a number between 1 and 4.")