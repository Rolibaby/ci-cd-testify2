#  Create a class called Human
class Human:
    leg_count = 4  # Add an Attribute leg_count with the value of 4
    can_walk = True  # Add another Attribute can_walk with the value of True

    def __init__(self,name):
        self.name = name

# Create a method called get_description, the method should print "This is human"
    def get_description(self,description):
       self.description = description
# Create another method that return the leg count, the name of the method is your choice
    def your_choice(self,count):
        self.count = count
        return count


people = Human("people")
print("people",people.leg_count,people.can_walk)
people.get_description("This is Human")
print(people.description)
people.your_choice(5)
print("New Leg count",people.count)
print("\nLeg count",people.leg_count)


