# Class creation
class myClass:
    # Private variable and method
    __privateVar = 27

    def __privMethod(self):
        print("SHHHH! This is private")
#Function to print the value of the private variable
    def hellO(self):
        print("Private Variable:", myClass.__privateVar)
# Method Call
foo = myClass()
foo.hellO()
foo.__privMethod()