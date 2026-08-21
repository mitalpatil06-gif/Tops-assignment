# task : 1  Create a Python dictionary called playlist_prices with at least 5 key-value pairs where 
#           the key is a Spotify playlist name (as a string) and the value is the playlist's price 
#           (as an integer) Print the dictionary.
"""
playlist_prices={
    "Bollywood Hits": 150,
    "Taylor Swift": 250,
    "Arijit Singh":300,
    "Party Mix":350,
    "Trending Hits":450
}
print(playlist_prices)
"""

# task : 2 Write a function update_playlist_price(playlist, new_price) that updates the price of a given playlist in the playlist_prices 
#          dictionary. Test it by updating the price of any one playlist and printing the updated dictionary.

"""
playlist_prices={"Bollywood Hits": 150,"Taylor Swift": 250,"Arijit Singh":300,"Party Mix":350,"Trending Hits":450}
def update_playlist_price(playlist,new_price):
    
    playlist_prices[playlist] = new_price

    update_playlist_price("Trending Hits", 200)

print(playlist_prices)
"""
# task :3  Remove a playlist from the playlist_prices dictionary using the del statement. 
#          Print the dictionary after deletion to confirm the change.
"""
playlist_prices={"Bollywood Hits": 150,"Taylor Swift": 250,"Arijit Singh":300,"Party Mix":350,"Trending Hits":450}
playlist_prices.pop("Party Mix")
print(playlist_prices)
"""
# task : 4 Given two sets: set1 contains the names of restaurants you have ordered from on Zomato, and 
# set2 contains the names of restaurants you have ordered from on Swiggy, find and print the 
# union and intersection of these sets.<br><br><em><strong>Hint:</strong> Use the union() 
# and intersection() methods of Python sets.</em>
"""
s1={"Domino's Pizza", "KFC", "McDonald's", "Burger King", "Subway"}
s2={"Pizza Hut", "KFC", "Burger King", "Domino's Pizza", "Starbucks"}
print("Union:", s1.union(s2))
print("Intersection:", s1.intersection(s2))
"""