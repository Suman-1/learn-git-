# class inheritance


class Vehicle:

    def __init__(self, VIN, manufacturer, weight):  # this is the constructor method
        self.vehicle_number = VIN
        self.manufacturer = manufacturer
        self.weight = 450

        # define the constructor method
        # then

    def Getweight(self):
        return self.weight

    def Getmanufacturer(self):
        return self.manufacturer

    def VechileType(self):
        pass


class car(Vehicle):
    def __init__(self, VIN, manufacturer, weight, seats):
        self.vehicle_number = VIN
        self.weight = weight
        self.manufacturer = manufacturer
        self.seats = seats

    def NumberOfSeats(self):
        return self.seats

    def Vehicle_Type(self):
        return 'car'


class Truck(Vehicle):
    def __init__(self, VIN, manufacturer, weight, capacity):
        self.vehicle_number = VIN
        self.weight = weight
        self.manufacturer = manufacturer
        self.capacity = capacity

    def transportCapacity(self):
        return self.capacity

    def Vehicle_Type(self):
        return 'Truck'


a = car('ABC', 'Land Rover', 1000, 4)
b = Truck('nabl', 'evogue', 213131, 100000)
c = car('SAM', 'Ford', 27323, 12)
d = Truck('kjasg', 'Eicher', 4383, 64836486)


for v in [a, b, c, d]:
    print(v.Getmanufacturer(), v.Vehicle_Type())

print(a.Getweight(), b.Getmanufacturer(), c.seats, d.transportCapacity())
