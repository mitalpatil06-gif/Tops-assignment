# Section C — Mini Capstone Project
#Mini Project: Food Delivery Order Management Console
"""
Objective:
Build a console-based food delivery order management system that combines OOP, file
handling, functions, and exception handling into a single working application. The system must
allow a user to place orders, view all past orders, and search for a specific order — with all data
saved to and reloaded from a JSON file.
Your project must:

1. The program must be menu-driven with at least four options: (1) Place New Order, (2) View All Orders, (3) Search Order by ID, (4) Exit.
2. Define a class Order with attributes: order_id (auto-generated), customer_name, items (list), total_amount, and status ('Pending' by default).
3. On startup, load all existing orders from orders.json; save the updated orders list back to the file after every new order is placed.
4. Validate all user inputs — catch non-numeric amounts, empty name fields, and missing file errors — and display a clear message without crashing.
5. Display all orders in a formatted table showing order ID, customer name, item count, total amount, and status; highlight orders with status 
   'Delivered' differently in the output.
"""
"""
import json

class Order:
    def __init__(self, order_id, customer_name, items, total_amount, status='Pending'):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount
        self.status = status

    def display_info(self):
        print(self.order_id, self.customer_name, len(self.items), self.total_amount, self.status)

def load_orders():
    orders = []

    try :
        with open ("orders.json","r") as file:
            data = json.load(file)

            for order_data in data:
                new_order = Order(
                    order_data["order_id"],
                    order_data["customer_name"], 
                    order_data["items"],
                    order_data["total_amount"],
                    order_data["status"]
                )
                orders.append(new_order)
    except FileNotFoundError:
        orders = []

    return orders

def save_orders(orders):
    data = []

    for order in orders:
        data.append({
            "order_id": order.order_id,
            "customer_name": order.customer_name,
            "items": order.items,
            "total_amount": order.total_amount,
            "status": order.status
        })

    with open("orders.json", "w") as file:
        json.dump(data,file)

def place_order(orders):
    customer_name = input("Enter customer name: ")

    if customer_name.strip() == "":
        print("Customer name cannot be empty.")
        return
    items = input("Enter items (comma-separated): ").split(",")

    try:
        total_amount = float(input("Enter total amount: "))
    except ValueError:
        print("Please enter a valid numeric amount.")
        return

    if len(orders) == 0:
        order_id = 1
    else:
        order_id = order_id[-1].order_id + 1

    order = Order(order_id, customer_name, items, total_amount)
    orders.append(order)

    save_orders(orders)

    print("Order placed successfully!")
    print("Order ID:", order_id)

def view_orders(orders):
    if len(orders) == 0:
        print("No orders found.")
        return

    print("\n-----All Orders-----")
    print("ID\tCustomer Name\tItem Count\tTotal Amount\tStatus")
    print("-----------------------------------------------")

    for order in orders:
        if order.status == "Delivererd":
            print("*",order.order_id, "\t",order.customer_name, "\t", len(order.items), "\t", order.total_amount, "\t", order.status)

        else:
            print(order.order_id, "\t",order.customer_name, "\t", len(order.items), "\t", order.total_amount, "\t", order.status)

def search_order(orders):
    try:
        order_id = int(input("Enter order ID: "))
    except ValueError:
        print("Please enter a valid order ID.")
        return

    for order in orders:
        if order.order_id == order_id:
            print("\n-----Order Details-----")
            print("Order ID:", order.order_id)
            print("Customer Name:", order.customer_name)
            print("Items:", order.items)
            print("Total Amount:", order.total_amount)
            print("Status:", order.status)
            return

    print("Order not found.")

orders = load_orders()

while True:
    print("\n1. Place New Order")
    print("2. View All Orders")
    print("3. Search Order by ID")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue

    if choice == 1:
        place_order(orders)

    elif choice == 2:
        view_orders(orders)

    elif choice == 3:
        search_order(orders)

    elif choice == 4:
        print("Thank you for using the Food Delivery Order Management System.")
        break

    else:
        print("Invalid choice. Please try again.") 
"""

