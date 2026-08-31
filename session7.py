# Task :1 Write a Python script that checks if a user's entered age is 18 or above and prints 'Eligible 
#         for IPL ticket booking' if true, otherwise prints 'Not eligible'.
"""
age=int(input("enter the age : "))

if age>18:
    print('Eligible for IPL ticket booking')
else:
    print('Not eligible')"""

# Task :2 Create a Python program that takes the number of followers as input and uses if, elif, and else to print 
#         'Micro Influencer' if followers < 10,000, 'Rising Star' if between 10,000 and 100,000, and 'Celebrity' if above 100,000.
"""
followers=int(input("enter the number of followers"))

if followers < 10000:
    print("Micro Influencer")
elif followers <=100000:
    print("Rising star")
else:
    print("celebrity")
"""
# Task : 3  Build a Python script that asks the user for their Zomato order total and prints 'Apply Free Delivery' if total is above 299, 
#          'Add more items for free delivery' if between 200 and 299, else 'Delivery charges apply'.
"""
order_total=int(input("Enter Zomato total order : "))

if order_total > 299:
    print("Apply Freee Deliver")
elif order_total>=200:
    print("Add more items for delivery")
else:
    print("Deliver charges apply")
"""
# Task : 4  Write a Python program using nested if statements: take a user's entered Flipkart cart value and payment method 
#           ('UPI', 'Card', 'Cash'). If the cart value is above 1000 and payment method is 'UPI', print 'Eligible for 10% cashback'; 
#           if above 1000 and payment is not 'UPI', print 'Eligible for 5% cashback'; else print 'No cashback'.
"""

cart_value=int(input("enter the cart value :"))
payment_method=input("enter the pyment method (UPI/Card/Cash) : ")

if cart_value > 1000:
    if payment_method=="UPI":
        print("Eligible for 10% cashback")
    else:
        print("Eligible for 5% cashback")
else:
    print("No cashback")
"""