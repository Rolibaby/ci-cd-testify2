# Create a class called  Hunt
class Hunt:
    __weapon = "Assault Rifle"  # Private attribute

    def get_weapon(self):  # method get_weapon()
        return "Not Available: " + self.__weapon  # returns "Not Available in the class


# Instantiate an object of the Hunt class
hunt = Hunt()
# Print the value of get_weapon() from the object instance
print(hunt.get_weapon())
