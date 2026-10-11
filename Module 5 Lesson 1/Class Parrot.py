#Create a Class
class Parrot:
    #Class attributes
    species = "bird"

    #Create init
    def __init__(self, name, age):
        #Initialize the attributes
        self.name = name
        self.age = age

#Parrot Class Initialization
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu is a {}".format(blu.species))
print("Woo is a {}".format(woo.species))

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
