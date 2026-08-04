# Task :1

a = 100
print("number of flowers :",a)
print(type(a))

b = 7.5
print("average rating :",b)
print(type(b))

c = "spotify" 
print("my favorite app's name:",c)
print(type(c))

d = "true" 
print("is_premium_user:",d)
print(type(d))

# Task : 2

a=int(input("enter the zomato order price:"))
gst = a*0.18

final_bill_amount = a + gst

print("final_bill_amount",float(final_bill_amount))

# Task : 3

prices =["199.99","299.5","150"]

a = float(prices[0])
b = float(prices[1])
c = float(prices[2])

Total = a + b + c

print("a value coverted into float:",a)
print("b value coverted into float:",b)
print("c value coverted into float:",c)
print("Total cart value:",Total)

# Task 4:

is_discount_amount ="order_amount"
order_amount = 750
if order_amount > 500:
    print(True)
else:
    print(False)
order_amount = 450
if order_amount > 500:
    print(True)
else:
    print(False)


# Task 5:

ratings = ['4.5', '3.0', '5', '4.2']

float_ratings = []

for rating in ratings:
    float_ratings.append(float(rating))

highest_rating = max(float_ratings)

print("Highest rating:", highest_rating)
