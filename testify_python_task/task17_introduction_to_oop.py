# Create a Class called Human
class Human:
    name = "intelligent"
    group = "Female"

    def get_name_group(self):
        return self.name + " vibrant " + self.group


# initialize the class
intelligent = Human()
print(intelligent.name, intelligent.group, intelligent.get_name_group())

