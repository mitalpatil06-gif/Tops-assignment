# task : 1 Write a lambda function that takes a price in rupees and returns the price after adding 18% GST. 
#          Test it on the prices 100, 250, and 500.
"""
gst_price = lambda price : price + (price*0.18)

print(gst_price(100))
print(gst_price(250))
print(gst_price(500))
"""

# task : 2 Given a list of song titles from Spotify with extra spaces and inconsistent casing, use map() and a lambda function 
#         to clean each title so that it is stripped of spaces and converted to title case (e.g., ' shape OF you ' → 'Shape Of You').
"""
l1=["shape of you"," kesariya","BLINDING LIGHTS","excuess"]
songs = list(map(lambda l1 : l1.strip().title(),l1))
print(songs)
"""

# task : 3  Use filter() and a lambda function to extract only those Flipkart product names from a list that start with the letter 'S' (case-insensitive).
"""
l1 = ["shoes","laptop","shirt","mobile","saree","watch"]
result = list(filter(lambda l1: l1.lower().startswith("s"),l1))
print(result)
"""

# task : 4  Given a list of order amounts from a Zomato cart [120, 340, 560, 80], use reduce() from functools to calculate the total bill amount. 
"""
from functools import reduce

orders = [120,340,560,80]

total_bill = reduce(lambda x,y: x+y,orders)

print("Total bill amount:",total_bill)
"""

# task : 5 Use ChatGPT or Copilot to generate a Python code snippet that uses map(), filter(), and reduce() together to process a list of numbers: 
#  first double each number, then filter to keep only numbers greater than 100, and finally sum the result. Paste and test the generated code with the list [40, 60, 80, 120].
"""
from functools import reduce 
numbers = [ 40,60,80,120]

doubled = list(map(lambda x: x*2,numbers))
filtered = list(filter(lambda x: x > 100,doubled))

total = reduce(lambda x, y: x+y,filtered)
print(total)
"""
