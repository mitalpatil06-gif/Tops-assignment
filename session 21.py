# task : 1 Create a Python class called Product with a method get_discount() that returns 0. Write a subclass called Electronics that 
#          overrides get_discount() to return 10.
"""
class product:
    def get_discount(self):
        return 0

class electronics(product):
    def get_discount(self):
        return 10

p = product()
p.get_discount()

e = electronics()
e.get_discount()

a = [product(), electronics()]

for i in a:
    print(i.get_discount())
"""

# task : 2 Build a class FoodOrder with a method calculate_total() that returns the base price. Create a subclass ZomatoOrder that overrides 
#          calculate_total() to add a 5% delivery charge.
"""
class foodorder:
    def calculate_total(self,price):
        return price

class zomatoorder(foodorder):
    def calculate_total(self, price):
        return price + (price * 0.05)

f = foodorder()
print(f.calculate_total(500))

z = zomatoorder()
print(z.calculate_total(750))
"""

# task : 3 Write a function show_bonus(employee) that takes any object with a bonus() method and prints the result. Test it with two classes: 
#        Influencer (bonus returns 2000) and BrandManager (bonus returns 5000), demonstrating polymorphism.
"""
class Influencer:
    def bonus(self):
        return 2000

class BrandManager:
    def bonus(self):
        return 5000

def show_bonus(employee):
    print(employee.bonus())

i = Influencer()
b = BrandManager()

show_bonus(i)
show_bonus(b)
"""

# task : 4 Given this code: class User: def get_status(self): return 'active' class PremiumUser(User): pass. Update PremiumUser to override get_status() 
#          so it returns 'premium'. Then, create one User and one PremiumUser and print their statuses.<br><br><em><strong>Hint:</strong> Use the same 
#          method name in both classes to override.</em>
"""
class User:
    def get_status(self):
        return "active"


class PremiumUser(User):
    def get_status(self):
        return "premium"


u = User()
p = PremiumUser()

print(u.get_status())
print(p.get_status())
"""