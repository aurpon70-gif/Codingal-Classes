class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        
        total_fare = base_fare + (base_fare * 0.10)
        return total_fare

my_bus = Bus("School Bus", 50)

print(f"Total Bus Fare: INR {my_bus.fare()}")