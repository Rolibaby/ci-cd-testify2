# Create a class called "Human"

class Human:
    leg_count = 4  # Add an Attribute leg_count with the value of 4
    can_walk = True  # Add another Attribute can_walk with the value of True

    def __init__(self, name):
        self.name = name


gorilla = Human("Gorilla")
teddy = Human("TeddyBear")

print(gorilla.name)
print(teddy.name)
print(gorilla.can_walk)
print(teddy.leg_count)
