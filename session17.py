# task : 1 Use the math module to calculate the square root, factorial, and value of pi for given numbers, and print each result.
"""
import math as m

number = 8

print("Square root : ", m.sqrt(number))
print("Factorial : ", m.factorial(number))
print("Value of pi : ", m.pi)
"""

# task : 2 Write a script that lists all files in your current directory using the os module, and prints only those files with a .jpg or .png 
#          extension.<br><br><em><strong>Hint:</strong> Use os.listdir() and string methods to filter file names.</em>
"""
import os 

files = os.listdir()

found = False

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        print(file)
        found = True

if found == False:
    print("No JPG or PNG files found.")
"""

# task : 3 Create a Python program that accepts a date in 'YYYY-MM-DD' format from the user and displays the day of the week using the datetime module.
"""
from datetime import datetime 

date = input("enter date(YYYY-MM-DD): ")

date = datetime.strptime(date,"%Y-%m-%d")
print("Day: ", date.strftime("%A"))
"""

# task : 4 Build a simple custom module named insta_utils.py with a function format_follower_count(n) that returns '1.5K' for 1500 and '2.3M' for 2300000. 
#          Import and use this function in another script to display formatted counts for 3 sample numbers.

"""
First, see the insta_utils.py file , then see the main.py file 
"""
# task : 5 Create a new virtual environment using venv, activate it, and install the statistics and requests packages via pip. Then, write a script that uses 
#          statistics.mean() to calculate the average of a list of numbers.