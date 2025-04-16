class Car:
    def move(self):
        print("Driving ")

class Plane:
    def move(self):
        print("Flying")

class Boat:
    def move(self):
        print("Sailing")

# List of different vehicle/animal objects
vehicles = [Car(), Plane(), Boat()]

# Call move() on each one
for vehicle in vehicles:
    vehicle.move()