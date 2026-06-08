# 1. Create a function to print first 10 natural numbers.
def print_first_10():
    for i in range(1, 11):
        print(i)

# 2. Create a function to calculate sum of first N natural numbers.
def sum_n_natural(n):
    return sum(range(1, n + 1))

# 3. Create a function to reverse a number.
def reverse_number(n):
    return int(str(n)[::-1])

# 4. Create a function to count digits in a number.
def count_digits(n):
    return len(str(abs(n)))

# 5. Create a function to check palindrome number.
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 6. Create a function to generate Fibonacci series.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# 7. Calculator Using Functions
def calculator():
    op = input("Enter operation (+, -, *, /): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    if op == '+': print(f"Result: {a + b}")
    elif op == '-': print(f"Result: {a - b}")
    elif op == '*': print(f"Result: {a * b}")
    elif op == '/':
        try:
            print(f"Result: {a / b}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

# 8. Create a text file and store student details.
def store_student(name, marks):
    with open("students.txt", "a") as f:
        f.write(f"{name}: {marks}\n")

# 9. Read data from a file.
def read_students():
    with open("students.txt", "r") as f:
        print(f.read())

# 10. Handle division by zero using exception handling.
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# 11. Create a Student class with name and marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
