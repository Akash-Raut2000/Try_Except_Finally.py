# Try, Except, and Finally: Handling Exceptions in Python

# Example 1: Basic Try-Except
try:
    # Code that may raise an exception
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError as e:
    # Handling the specific exception
    print("Error:", e)

# Example 2: Catching Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Error: Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Example 3: Using Finally
try:
    file = open("example.txt", "w")
    file.write("Hello, world!")
except IOError as e:
    print("File error:", e)
finally:
    # This block will always execute
    print("Closing the file.")
    file.close()

# Example 4: Try-Except-Else-Finally
try:
    num = int(input("Enter another number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter a valid integer.")
else:
    # Executes if no exception occurs
    print("Division successful! Result:", result)
finally:
    # Always executes regardless of exceptions
    print("Execution complete.")
