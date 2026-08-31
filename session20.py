# task : 1 Create a Python class called Product with a private attribute _price. Initialize _price in the constructor and write a method to 
#          display its value.
"""
class product:
    def __init__(self,price):
        self.price = price

    def display_price(self):
        print("Price :", self.price)

p = product(500)

p.display_price()
"""

# task : 2 Add getter and setter methods for the _price attribute in your Product class to safely access and update the price. Make sure the 
#          setter prevents setting a negative price.<br><br><em><strong>Hint:</strong> Raise a ValueError if the new price is less than zero.</em>
"""
class product:
    def __init__(self,price):
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self,new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.price = new_price

p = product(670)

print("Old price :",p.get_price())

p.set_price(890)
print("New price :",p.get_price())
"""

# task : 3 Build a class called Playlist that has a private attribute _songs (a list of song names). Write methods to add a song, remove a song, and get the 
#          current list of songs using proper encapsulation.
"""
class playlist:
    def __init__(self):
        self.songs = []

    def get_songs(self):
        return self.songs

    def add_song(self,song):
        self.songs.append(song)

    def remove_song(self,song):
        self.songs.remove(song)

p = playlist()
p.add_song("For a reason")
p.add_song("Yehh fitoor tera")
p.add_song("You're U Tho")
print("Songs are :",p.get_songs())

p.remove_song("For a reason")
print("After removing song :")
print(p.get_songs())
"""

# task : 4 Create an abstract class PaymentMethod with an abstract method pay(amount). Then, create two subclasses: UPI and CreditCard, each implementing the pay
#          method with a print statement showing how the payment would be processed.<br><br><em><strong>Hint:</strong> Use the abc module for abstraction.</em>
"""
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(PaymentMethod):
    def pay(self,amount):
        print("Payment of", amount, "processed through UPI")

class creditcard(PaymentMethod):
    def pay(self,amount):
        print("Payment of", amount, "processed through credit card")

u = UPI()
u.pay(650)

c = creditcard()
c.pay(1500)
"""