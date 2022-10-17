# Create a function that accepts two numbers,
print("\nFunction that accept 2 numbers")


def add(num1=20, num2=10):
    result = num1 + num2  # adds the numbers
    print("Result:", result)  # prints out the result in the console.


add()  # Invoke/call the functions
add(8, 7)  # Invoke/call the functions and passing parameters

# Create a function that return the string value "Testify Python"
print("\nFunction that return Testify Python")


def greet(name):
    print("Testify", name)
    return name


greet("Python")  # Invoking the function
