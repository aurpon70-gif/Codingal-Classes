# Define the BMW class
class BMW:
    def fuel_type(self):
        print("BMW fuel type: Petrol / Electric")

    def max_speed(self):
        print("BMW max speed: 250 km/h")

# Define the Ferrari class
class Ferrari:
    def fuel_type(self):
        print("Ferrari fuel type: Petrol")

    def max_speed(self):
        print("Ferrari max speed: 340 km/h")

# Function to demonstrate polymorphism
def display_car_details(car_obj):
    car_obj.fuel_type()
    car_obj.max_speed()

# Create objects for both classes
bmw_car = BMW()
ferrari_car = Ferrari()

# Calling the polymorphic function with different objects
print("--- BMW Car Details ---")
display_car_details(bmw_car)

print("\n--- Ferrari Car Details ---")
display_car_details(ferrari_car)