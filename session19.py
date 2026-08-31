# task : 1 Define a Python class called Song with attributes title, artist, and duration (in seconds), and use the __init__() constructor 
#          to initialize these values when creating an object.
"""
class song:
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration

a = song("For A Reason","Karan Aujla",180)
print("Song name :",a.title)
print("Artist name :",a.artist)
print("Duration in second :",a.duration)
"""

# task : 2 Create an object of the Song class for your favorite track from Spotify, and print out its title and artist using object attributes.
"""
class myfavoritesong:

     def __init__(self,title,artist):
          self.title = title
          self.artist = artist

a = myfavoritesong("Yeh Fitoor Mera","Arijit Singh")

print("My favorite song :",a.title)
print("Artist of the song :",a.artist)
"""

# task : 3 Add a method play_preview(self) to your Song class that prints 'Playing 30-second preview of [title] by [artist]'. Call this method for your Song object.
"""
class song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def play_preview(self):
        print("Playing 30-second preview of", self.title, "by", self.artist)

s = song("Kesariya","Arijit Singh")
s.play_preview()
"""

# task : 4  Create a class called FoodOrder with attributes restaurant_name, items (a list), and total_price. Add a method add_item(self, item, price) that 
#           adds the item to the items list and updates total_price. Demonstrate by creating a FoodOrder object and adding two items like you would on Zomato.
"""
class foodorder:
    def __init__(self,restaurant_name,items,total_price):
        self.rastaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def add_item(self,item,price):
        self.items.append(item)
        self.total_price = self.total_price + price

order = foodorder("Dominos", [], 0)
order.add_item("Pizza",199)
order.add_item("Garlic Bread",99)

print(order.rastaurant_name)
print(order.items)
print(order.total_price)
"""

# task : 5 Refactor your Song class so that it also tracks a play_count attribute (starting at 0), and add a method increment_play_count(self) that increases play_count 
#        by 1 each time it's called. Show how you would use this to count how many times a user plays a song.<br><br><em><strong>Hint:</strong> Call increment_play_count()
#        multiple times and print play_count to see the update.</em>
"""
class song:
    def __init__(self,title,artist):
        self.title = title 
        self.artist = artist
        self.play_count = 0

    def increment_play_count(self):
        self.play_count = self.play_count + 1

a = song("Rabbta","Arijit Singh")

a.increment_play_count()
a.increment_play_count()
a.increment_play_count()
a.increment_play_count()

print("Play count :",a.play_count)
"""