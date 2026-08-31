# task : 1  Use open() in write mode to create a file called my_playlist.txt and write the names of 5 songs 
#           you listened to this week, each on a new line.
"""
with open("my_playlist.txt","w") as f:
    f.write("kesariya.\n")
    f.write("believer.\n")
    f.write("shape of you.\n")
    f.write("blining lights.\n")
    f.write("excuses.\n")
    f.close()
"""

# task : 2 Read the my_playlist.txt file you created and print each song name in uppercase using Python file handling.
"""
with open("my_playlist.txt","r") as f:
    contaxt = f.readlines()

    print(contaxt)
    f.close()
"""
# task : 3 Download a sample CSV file of IPL cricket match scores (or create your own with columns: Match, Team1, Team2, Winner), 
#          then write Python code to read the CSV and print the name of the winning team for each match.
"""
import csv 

with open("ipl_matches.csv","r",encoding="utf-8",errors="ignore",newline="") as f:
    r = csv.reader(f)

    for i in r:
        print(i[3])
"""

# task : 4 Given a JSON file named user_profile.json containing details like username, followers, and bio (similar to an Instagram profile), 
#          use the json module to load the file and print the username and number of followers.
"""
import json

with open ("user_profile.json","r") as f:
    data = json.load(f)

print("Username:",data[0]["username"])
print("Followers:",data[0]["followers"])
"""

# task : 5  Use pathlib to check if a file called zomato_orders.json exists in your current directory, and print an appropriate message if it is 
#           found or not.<br><br><em><strong>Hint:</strong> Use Path('zomato_orders.json').exists() from the pathlib module.</em>.
"""
from pathlib import Path 

file = Path("zomato_orders.json")

if file.exists():
    print("file is found")

else:
    print("file is not found")
"""
