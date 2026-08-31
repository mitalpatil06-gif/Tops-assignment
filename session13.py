# task : 1  Write a recursive function in Python called reverse_string(s) that takes a string and 
#           returns it reversed (e.g., 'hello' becomes 'olleh').
"""
def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))
"""

# task : 2  Build a recursive function sum_playlist_durations(durations) that takes a list of song durations 
#          (in seconds) and returns the total duration, similar to how Spotify totals a playlist.
"""
def sum_playlist_duration(durations):
    if durations == []:
        return 0 
    return durations[0] + sum_playlist_duration(durations[1:])

durations = [180,240,200,300]

print(sum_playlist_duration(durations))
"""

# task : 3  Given the following code, identify whether the variable 'count' is local or global in each function, and explain what will be printed when run:
"""
count = 10
def update_count():
count = 5
print('Inside:', count)

update_count()
print('Outside:', count)
"""
"""
count=10
def update_count():
    count=5
    print('Inside:',count)

update_count()
print('outside:',count)"""

# explanation : count = 5 is a local variable inside the function, so it dose not change the global count = 10. Therefor,inside the function it prints 5, and 
#               outside the function it prints 10.

# task : 4  Create a recursive function count_likes(posts) that takes a nested dictionary representing Instagram posts and their replies (each with a 'likes' key), 
#           and returns the total number of likes across all posts and replies.<br><br><em><strong>Hint:</strong> Each reply can itself have more replies, so use recursion to sum likes at all levels.</em>
"""
posts={"posts1":{"likes": 100},
       "post2":{"likes": 50}
}

def count_likes(posts):
    total = 0

    for post in (posts.values()):
        total += post["likes"]

        if "replies" in post:
            total += count_likes(post["replies"])

    return total 
print(count_likes(posts))
"""

# task : 5  Write a Python script that demonstrates the lifetime of a local variable inside a function versus a global variable by printing their values before, during, and after a function call. Use variable 
#           names similar to 'user_status' and 'app_status', inspired by WhatsApp online/offline status.
"""
app_status = "offline"

def update_status():
    user_status = "online"
    print("During function - user_status:",user_status)
    print("During function - app_status:",app_status)

print("Before function - app_status:",app_status)

update_status()
print("After function - app_status:",app_status)
"""

