# Create a class called User
class User:
    __password = "password"  # private attribute called __password

    def get_password(self):  # method get_password()
        return self.__password  # returns self.__password


# Create another class called ActiveUser that inherits from the User class
class ActiveUser(User):

    def get_password(self):  # method get_password()
        return "*******"  # returns *******


user = User()
print("User:", user.get_password())
# Instantiate an object of the ActiveUser class
active_user = ActiveUser()
# Print the value of get_password() from the object instance
print("ActiveUser(User):", active_user.get_password())
