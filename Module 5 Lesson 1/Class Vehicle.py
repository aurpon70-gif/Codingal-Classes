#Create a Class
class Vehicle:
    #Create init
    def __init__(self, max_speed, mileage):
        #Initialize the attributes
        self.max_speed = max_speed
        self.mileage = mileage
#Object Creation
modelX = Vehicle(240, 18)
#Accessing Variables
print("Model Max Speed:", modelX.max_speed)
print("Model Mileage:", modelX.mileage)