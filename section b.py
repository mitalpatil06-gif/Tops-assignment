# Task 1: Delivery Fee Calculator 
# Build a console program that calculates and displays the final bill for a food delivery order 
# based on order value and delivery distance.
"""
1. Prompt the user to enter the order value (Rs ) and delivery distance (km) as separate inputs.
2. Apply these fee rules using conditional statements: free delivery if order value >= Rs 500; Rs 30
   fee if distance <= 5 km; Rs 60 fee if distance > 5 km.
3. Display the item total, delivery fee, and final amount payable in a clearly formatted output.
4. Handle the case where the user enters a negative distance or negative order value by printing
   an appropriate error message and stopping execution 
"""
# Solution :
"""
order_value = float(input("Enter the order value (Rs): "))
distance = float(input("Enter the delivery distance (km): "))

if order_value < 0 or distance < 0:
    print("Error: Order value and distance must be non-negative.")
    
elif order_value >= 500:
    delivery_fee = 0
    final_amount = order_value + delivery_fee

elif distance <= 5:
    delivery_fee = 30
    final_amount = order_value + delivery_fee
    
else:
    delivery_fee = 60
    final_amount = order_value + delivery_fee

print("\n-----Delivery Bill-----")
print("Item total    : Rs", order_value)
print("Delivery fee  : Rs", delivery_fee)
print("Final amount  : Rs", final_amount)
"""

# Task 2: Restaurant Menu Manager
#Build a menu management program that stores a restaurant's menu in a dictionary and lets the user interact with it through a looped console interface.

"""
1. Store at least 6 menu items in a dictionary; each item maps a dish name (key) to a nested dictionary with keys: price and category.
2. Provide three options in a loop: (1) View all items formatted as a numbered table, (2) Filter items by category, (3) Search for a dish by name and display its price.
3. Define a separate function for each of the three operations; call them from the main loop.
4. Keep the loop running until the user enters '0' to exit.
"""
"""
menu = {
    "Margherita Pizza": {"price": 250, "category": "MainCourse "},
    "Masala Dosa": {"price": 150, "category": "MainCourse"},
    "Chocolate Brownie": {"price": 120, "category": "Dessert"},
    "Veggie Burger": {"price": 200, "category": "MainCourse"},
    "Alio Olio Pasta": {"price": 220, "category": "MainCourse"},
    "Gulab Jamun": {"price": 80, "category": "Dessert"}
}
def view_all_items():
    print("\n-----Restaurant Menu-----")
    number = 1 

    for dish, details in menu.items():
        print(number, dish, "Rs", details["price"],  details["category"])
        number += 1

def filter_by_category():
    category = input("Enter category: ")

    print("\n-----Items in category:", category, "-----")

    for dish, details in menu.items():
        if details["category"].lower() == category.lower():
            print(dish, "Rs", details["price"])

def search_dish():
    dish_name = input("Enter dish name : ")

    if dish_name in menu:
        print("Dish :", dish_name)
        print("Price: Rs", menu[dish_name]["price"])
    else:
        print("Dish not found in the menu.")

while True:
    print("\n 1. View all items")
    print(" 2. Filter items by category")
    print(" 3. Search for a dish by name")  
    print("Exit")

    choice = int(input("Enter the choice :"))

    if choice == 0:
        print("Thanks for using the menu manager")
        break
    elif choice == 1:
        view_all_items()

    elif choice == 2:
        filter_by_category()

    elif choice == 3:
        search_dish()
    else:
        print("Invalid choice. Please try again.")
"""

# task : 3 Order History File Logger :
#Build a program that records food delivery orders to a JSON file and lets the user view all past orders, demonstrating file handling and exception handling together.
"""
1. Accept the following order details from the user: customer name, list of items
   (comma-separated input converted to a Python list), total amount, and order status.
2. Load the existing orders list from orders.json before adding the new order, then save the
   updated list back to the file — so all orders accumulate across runs.
3. Provide a 'View Orders' option that reads orders.json and prints each order in a readable
   format.
4. Use a try-except block to handle FileNotFoundError (first run, no file yet) and ValueError
   (non-numeric total amount).
"""
"""
import json 

try:
    with open("orders.json", "r") as file:
        orders = json.load(file)

except FileNotFoundError:
    orders = []


customer_name = input("Enter customer name: ")
items = input("Enter items (comma-separated): ").split(",")
total_amount = float(input("Enter total amount: "))
order_status = input("Enter order status: ")

order = {
    "customer_name": customer_name,
    "items":  items,
    "total_amount": total_amount,
    "order_status": order_status
}
orders.append(order)

with open("orders.json", "w") as file:
    json.dump(orders, file)


while True:
    print("\n1. Add Order")
    print("2. View Orders")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 3 :
        print("Thanks for using the order history logger.")
        break

    elif choice == 1:
        customer_name = input("Enter customer name: ")
        items = input("Enter items (comma-separated): ").split(",")
        total_amount = float(input("Enter total amount: "))
        order_status = input("Enter order status: ")

        order = {
            "customer_name": customer_name,
            "items":  items,
            "total_amount": total_amount,
            "order_status": order_status
        }
        orders.append(order)

        with open("orders.json", "w") as file:
            json.dump(orders, file)

        print("Order added successfully.")

    elif choice == 2:
        try:
            with open("orders.json","r") as file:
                orders = json.load(file)
            print("\n-----Order History-----")

            for order in orders:
                print("Customer Name:", order["customer_name"])
                print("Items:", ", ".join(order["items"]))
                print("Total Amount: Rs", order["total_amount"])
                print("Order Status:", order["order_status"])
                print("------------------------")
        except FileNotFoundError:
            print("No orders found.")
"""

# task 4 Delivery Rider OOP System
#Build an object-oriented system that models delivery riders using a class, stores multiple rider objects in a list, and persists their data to a CSV file.
"""
1. Create a Rider class with instance attributes: rider_id, name, status (default 'Available'), and
   total_deliveries (default 0).
2. Implement three methods: assign_order(order_id) — sets status to 'On Delivery' and prints a
   confirmation; complete_delivery() — increments total_deliveries, resets status to 'Available';
   display_info() — prints all rider details.
3. In the main program, create at least three Rider objects and provide a simple numbered menu
   to assign and complete orders for any rider selected by ID.
4. Save all rider data to riders.csv using the csv module when the user exits, and reload it at
   program start if the file exists.
"""
"""
import csv

class rider:
    def __init__(self,rider_id, name, status="Available",total_deliveries=0):
        self.rider_id = rider_id
        self.name = name
        self.status = status
        self.total_deliveries = total_deliveries

    def assign_order(self, order_id):
        self.status = "On Delivery"
        print("Order",order_id,"assigned to",self.name)

    def complete_delivery(self):
        self.total_deliveries += 1
        self.status = "Available"
        print("Delivery completed by",self.name)

    def display_info(self):
        print("Rider ID:", self.rider_id)
        print("Name:", self.name)
        print("Status:", self.status)
        print("Total Deliveries:", self.total_deliveries)

rider1 = rider(1, "Ram")
rider2 = rider(2, "Lakshman")
rider3 = rider(3, "Hanuman")

riders = [rider1, rider2, rider3]

def find_rider(rider_id):
    for rider in riders:
        if rider.rider_id == rider_id:
            return rider
    return None
try:
    with open("riders.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rider = find_rider(int(row["Rider ID"]))

            if rider is not None:
                rider.name = row["Name"]
                rider.status = row["Status"]
                rider.total_deliveries = int(row["Total Deliveries"])

except FileNotFoundError:
    print("No previous rider data found.")

while True:
    print("\n1. Assign Order")
    print("2. Complete Delivery")
    print("3. Display Rider Info")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        with open("riders.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Rider ID", "Name", "Status", "Total Deliveries"])
            for rider in riders:
                writer.writerow([rider.rider_id, rider.name, rider.status, rider.total_deliveries])
        print("Rider data saved successfully")
        break

    elif choice == 1:
        rider_id = int(input("Enter Rider ID: "))
        order_id = input("Enter Order ID: ")
        rider = find_rider(rider_id)
        if rider is not None:
            rider.assign_order(order_id)
        else:
            print("Rider not found.")

    elif choice == 2:
        rider_id = int(input("Enter Rider ID: "))
        rider = find_rider(rider_id)
        if rider is not None:
            rider.complete_delivery()
        else:
            print("Rider not found.")

    elif choice == 3:
        rider_id = int(input("Enter Rider ID: "))
        rider = find_rider(rider_id)
        if rider is not None:
            rider.display_info()
        else:
            print("Rider not found.")
"""