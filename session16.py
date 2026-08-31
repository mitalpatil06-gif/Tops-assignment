# task : 1 Use iter() and next() to manually loop through a list of 5 trending movies from BookMyShow and print each movie name one by one.
"""
movies=["Hanuman ansh","Toxic","Awarapan 2","Spider man","Insidious"]

movie = iter(movies)

print(next(movie))
print(next(movie))
print(next(movie))
print(next(movie))
print(next(movie))
"""
# task : 2 Create a playlist of 6 songs (as a list of strings) and use enumerate() to print each song with its position like Spotify's tracklist (e.g., '1. Kesariya').
"""
songs = ["kesariya","believer","shape of you","blinding lights","excuses","perfact"]

for position,song in enumerate(songs,start=1):
    print(f"{position}.{song}")
"""

# task : 3  Given two lists — one of food items and one of prices — use zip() to print each food item with its price like a Zomato menu (e.g., 'Pizza - ₹250').
"""
food_items = ["pizza","burger","pasta","sandwich"]
prices =[250,150,200,120]

for food,price in zip(food_items,prices):
    print(f"{food} - ₹{price}")

"""

# task : 4 Write a generator function called insta_posts_generator(posts) that takes a list of Instagram post captions and yields one caption at a time. Use next() to get 
#         and print the next post caption each time until all captions are printed.<br><br><em><strong>Hint:</strong> Use the yield keyword inside your function and handle 
#         StopIteration when all posts are done.</em>
"""
def insta_posts_generator(posts):
    for i in posts:
        yield i 

posts=["Good vibes","Sunshine and sweet vibes","Visiting cozy cafe"]
post = insta_posts_generator(posts)

try:
    print(next(post))
    print(next(post))
    print(next(post))

except StopIteration:
    print("All posts are printed.")
"""

# task : 5 Build a generator function called cashback_generator(transactions) that takes a list of Paytm transaction amounts and yields 5% cashback for each transaction. 
#          Print out the cashback values for all transactions.
"""
def cashback():
    yield 500*0.05
    yield 1000*0.05
    yield 2000*0.05
    yield 900*0.05

c = cashback()
print("Transaction 1 -->",next(c))
print("Transaction 2 -->",next(c))
print("Transaction 3 -->",next(c))
print("Transaction 4 -->",next(c))
"""