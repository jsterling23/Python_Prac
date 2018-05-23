class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.displayInfo()

    def displayInfo(self):
        print "Price: ${}. Speed: {}. Fuel: {}. Mileage: {}MPG. Tax: {}.".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

car1 = Car(11000, 50, "Full", 20)
car2 = Car(1000, 30, "Not Full", 5)
car3 = Car(9999, 87, "Full", 10)
car4 = Car(11000, 50, "Full", 20)

all_cars = car1,car2,car3,car4
print all_cars
