#  Create a class called Human
class Human:
    leg_count = 4  # Add an Attribute leg_count with the value of 4

    def get_gender(self):  # Add a method called get_gender() that returns "Unknown" in the Human class
        print("{Human: Unknown}")


class Man(Human):  # class called man that extends Human

    def get_gender(self):  # method that returns man
        print("{Gender: Man}")


class Woman(Human):  # class called woman that extends Human
    def get_gender(self):  # method that returns woman
        print("{Gender: Woman}")


human = Human()
human.get_gender()

man = Man()
man.get_gender()

woman = Woman()
woman.get_gender()

# Instantiate the Man and Woman classes
# Print out the value of get_gender() from the Man and Woman object instances
