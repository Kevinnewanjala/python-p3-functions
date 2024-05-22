#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

# Call the function
greet_programmer()

def greet(name):
    print(f"Hello, {name}!")

# Call the function
greet("programmer")


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# Call the function with the default parameter
greet_with_default()

# Call the function with a custom parameter
greet_with_default("John")


def add(num1, num2):
    return num1 + num2

# Example usage:
result = add(5, 3)
print(result)  # Output will be 8


def halve(number):
    if not isinstance(number, (int, float)):
        return None

    return number / 2

# Example usage:
result = halve(10)
print(result)  # Output will be 5.0

result = halve("hello")
print(result)  # Output will be None

