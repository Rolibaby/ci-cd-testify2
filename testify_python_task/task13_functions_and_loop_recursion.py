# Create a function that prints out "Hello World"
def hello_world():
    print("Hello World")
    return  # Stops the console from printing endlessly
    hello_world()  # Invoke the same function in it own body


hello_world()  # Invoke the function outside the function block
