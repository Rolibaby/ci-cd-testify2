#  Create a class called Human
class Human:
    leg_count = 4  # Add an Attribute leg_count with the value of 4
    people = "Unknown"

    def get_gender(self):  # Add a method called get_gender() that returns "Unknown" in the Human class
        print("\nHuman{", self.people, ",", self.leg_count, "}")


class Man(Human):  # Create another class called Man that extends Human
    def __init__(self, leg_count, people):
        self.leg_count = leg_count
        self.people = people


class Woman(Human):
    leg_count = 2
    people = "girls"


human1 = Human()
human1.get_gender()

man1 = Man("Male", "Female")
man1.get_gender()

woman1 = Woman()
woman1.get_gender()
