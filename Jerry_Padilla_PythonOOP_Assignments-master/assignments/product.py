class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'For Sale'

    def sell(self):
        self.status = "Sold"
        return self

    def add_tax(self, tax):
        self.tax = tax
        total_tax = self.price * self.tax
        self.price = self.price + total_tax
        return self

    def return_item(self, condition):
        self.condition = condition
        if self.condition == "defective":
            self.status = "Defective"
            self.price = 0
            return self
        elif self.condition == 'like new':
            self.status = 'For sale'
            return self
        elif self.condition == 'open box':
            self.status = 'Used'
            discount = self.price * 0.20
            self.price = self.price - discount
            return self
        else:
            self.status = 'Unknown'
            return self

    def displayInfo(self):
        print "Item: {}".format(self.item_name)
        print "Price: ${}".format(self.price)
        print "Weight: {}".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Status: {}".format(self.status)

item1 = Product(20,'Water',0.5,'S.Pellegrino')
item1.sell().add_tax(0.10).return_item('open box').displayInfo()
print item1
