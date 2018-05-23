class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def ride(self):
        self.miles += 8
        print "Riding 10 miles"
        return self
    def reverse(self):
        if self.miles - 5 < 0:
            print "Cannot go negative miles"
            return self
        else:
            self.miles -= 5
            print "Reversing 5 miles"
            return self
    def displayInfo(self):
        print "This bike cost: ${}. It has a max speed of {}MPH. It currently has {} miles on it.".format(self.price, self.max_speed, self.miles)
        return self

bike1 = Bike(233,25)
bike1.ride().ride().ride().reverse().reverse().reverse().reverse().reverse()
print (bike1.displayInfo())
