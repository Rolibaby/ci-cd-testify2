# create a class called Utilities
class Utilities:
    # create a static method called print_name which accepts parameter
    def print_name(electricity, water):
        return electricity + "," + water


Utilities.print_name = staticmethod(Utilities.print_name)  # static method
print("Utilities:", Utilities.print_name("electricity", "water"))
