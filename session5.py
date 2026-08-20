# task : 1  Create a list called playlist_ids with 5 integers representing Spotify playlist IDs, 
#           then use append() to add a new playlist ID at the end and print the updated list.

"""
playlist_ids=[ 101,102,103,104,105 ]
playlist_ids.append(106)
print(playlist_ids)
"""
# task: 2  Simulate a Flipkart shopping cart: start with a list cart_items containing 't-shirt', 'shoes'. 
#          Use extend() to add ['jeans', 'cap'] to the cart, then print the final list of items.
"""
cart_list=['t-shirt','shoes']
cart_list.extend(['jeans','cap'])
print(cart_list)
"""
# task : 3  Write a function remove_last_item(order_list) that pops the last item from 
#           a Zomato order list and returns the removed item. Test it with a sample order_list.
"""
def remove_last_item( ):
    order_list=['pizza','pasta','fries','cold coffee']
    remove_last_item = order_list.pop()
    print(order_list)
remove_last_item()
"""
# task :4 Create a tuple called insta_filters with 4 Instagram filter names. Try to update the second filter and observe what error you get.
#         Explain in a comment why this happens.<br><br><em><strong>Hint:</strong> Tuples are immutable, so direct assignment won't work.</em>
"""
insta_filters=('glowness','sunset','cloud','bright')
insta_filters[1]= 'vintage'
# error: TypeError
# Tuples are immutable, so their elements cannot be changed directly.
"""
# task : 5 Given two scenarios — storing a user's favorite genres (which may change) and storing a fixed set of IRCTC train 
# classes ('Sleeper', 'AC 3 Tier', 'AC 2 Tier') — choose whether to use a list or tuple for each. Write one sentence explaining your choice for both.

"""
favorite_genres = ['pop','rock','classical']  ---> # list , because it can change.
train_classes = ('sleeper','AC 3 Tier','AC 2 Tier') ---> # tuple, because it is fixed.
"""

