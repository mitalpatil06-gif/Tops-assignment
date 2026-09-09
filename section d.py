# Section D — AI-Augmented Learning
"""
STEP 1 · BUILD WITH AI
Use an AI tool of your choice (ChatGPT, Claude, GitHub Copilot, etc.) to help you write a Python
program that:
-> Accepts a list of food items and their prices for a delivery order and calculates the itemised
   subtotal.
-> Adds an 18% GST charge and a delivery fee (Rs 30 flat) to produce a final bill amount.
-> Applies a 10% loyalty discount on the subtotal if the customer has placed more than 5 previous
   orders — taken as a user input.
->Prints a formatted receipt showing each line item (subtotal, GST, delivery fee, discount if
  applicable, and final amount payable) and handles invalid inputs such as negative prices or
  non-numeric order counts.

STEP 2 · TEST & DEBUG (WITHOUT AI)
Then, working without AI, test the code and find at least one bug, limitation, or improvement in
the AI's solution. Fix it yourself.
SUBMIT 
1 The exact prompt(s) you gave the AI tool.
2 The AI's original code and your corrected version.
3 A 3–4 line note explaining what you changed and why the AI's version needed it
"""

"""
items = []
prices = []

try:
    number_of_items = int(input("Enter number of food items: "))

    for i in range(number_of_items):
        item = input("Enter food item: ")
        price = float(input("Enter price: "))

        while price < 0:
           print("Price cannot be negative.")
           price = float(input("Enter price again: "))
        

        items.append(item)
        prices.append(price)

    if len(items) == number_of_items:
        previous_orders = int(input("Enter number of previous orders: "))

        subtotal = sum(prices)
        gst = subtotal * 0.18
        delivery_fee = 30

        if previous_orders > 5:
            discount = subtotal * 0.10
        else:
            discount = 0

        final_amount = subtotal + gst + delivery_fee - discount

        print("\n----- Food Delivery Receipt -----")

        for i in range(len(items)):
            print(items[i], "Rs", prices[i])

        print("---------------------------------")
        print("Subtotal       : Rs", subtotal)
        print("GST (18%)      : Rs", gst)
        print("Delivery Fee   : Rs", delivery_fee)
        print("Discount       : Rs", discount)
        print("Final Amount   : Rs", final_amount)

except ValueError:
    print("Invalid input. Please enter a valid number.")
"""

"""
The AI code stopped the program when a negative price was entered.
I found that the user should get another chance to enter a valid price.
I replaced the break with a while loop to ask for the price again.
This makes the program more user-friendly and handles negative prices better.
"""