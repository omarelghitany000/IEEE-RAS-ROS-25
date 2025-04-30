class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        if item in self.items:
            self.items[item] += price
        else:
            self.items[item] = price    

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())

my_cart = ShoppingCart()
my_cart.add_item("Apple", 5)
my_cart.add_item("Banana", 3)

print("Total price:", my_cart.total_price(), "EGP")

my_cart.remove_item("Apple")
my_cart.remove_item("orange") # Item not in cart

print("Total price:", my_cart.total_price(), "EGP")