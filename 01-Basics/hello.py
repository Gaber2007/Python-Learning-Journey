"""
Project: Personal Profile & Smart Calculator
Level: Python Basics
Topics: Variables, Data Types, Input, Output, Operators, Formatting
"""

print("=" * 45)
print("       PYTHON LEARNING JOURNEY")
print("=" * 45)

# Personal information
name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))
city = input("Enter your city: ").strip()

# Basic calculations
next_year_age = age + 1
age_in_months = age * 12
age_in_days = age * 365

# Display profile
print("\n" + "-" * 45)
print("             YOUR PROFILE")
print("-" * 45)

print(f"Name            : {name}")
print(f"Age             : {age} years")
print(f"City            : {city}")
print(f"Age next year   : {next_year_age}")
print(f"Age in months   : {age_in_months}")
print(f"Approx. days    : {age_in_days}")

# Smart calculator
print("\n" + "=" * 45)
print("             SMART CALCULATOR")
print("=" * 45)

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("\nResults:")
print(f"Addition       : {first_number + second_number}")
print(f"Subtraction    : {first_number - second_number}")
print(f"Multiplication : {first_number * second_number}")

if second_number != 0:
    print(f"Division       : {first_number / second_number:.2f}")
else:
    print("Division       : Cannot divide by zero!")

print("\nThank you for practicing Python!")
