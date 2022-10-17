# Declare a global variable with name as language and the value as "Python"
print("\nGlobal Variable")

language1 = "Python"  # Global Variable


# Create a function, in the function declare a variable with name as language and value as "Java"
def programming():
    language = "Java"  # Local Variable
    print("Language1", language1, "language", language)
    print(language)


def strategy():
    framework = "Selenium"  # Local Variable
    print("Framework:", framework)
    print(framework)


print(language1)
programming()
strategy()
