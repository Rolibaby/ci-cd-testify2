# create a class called Utilities
class Utilities:
    # create a static method called print_name which accepts parameter
    
    def print_name(electricity):
        return electricity 

    @staticmethod
    def print_name2(water):
        return water


Utilities.print_name = staticmethod(Utilities.print_name)  # static method
print("The name of my Electricty company is ", Utilities.print_name("Apapa Electricity"))
print("My water is ",Utilities.print_name2("Eva table water"))
