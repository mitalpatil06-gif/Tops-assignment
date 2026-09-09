# SCENARIO 1 
#You are building a food delivery app that tracks four values per order: the order total (Rs499.50), the delivery distance (7.3 km), 
#the payment method ('UPI'), and whether the restaurant is currently accepting orders (True).

"""Question: Identify the correct Python data type for each of the four values above. Then explain
why assigning the wrong type — for example, storing Rs 499.50 as an integer — would cause an
incorrect result when applying a 10% discount calculation."""

# Answer :
"""
The order total rs.499.50 is a float because it has a decimal value. The delivery distance 7.3 km is also a float because it has a decimal 
value. The payment method 'UPI' is a string because it is text. The value True is a boolean because it shows whether the restaurant is accepting 
orders. If we store rs.499.50 as an integer , it will give a wrong result when applying a 10% discount because the decimal part will be lost.
"""

# SCENARIO 2 
#You are developing a restaurant menu system. A teammate suggests storing the menu as a list of tuples like 
#[('Paneer Burger', 180, 'Snacks'), ('Masala Dosa', 90, 'Breakfast')], while you prefer a dictionary where each dish name is the key.

"""Question: Compare these two data structures for looking up a dish price by name. Which gives
faster and more readable access, and why? Describe one limitation of the list-of-tuples
approach that the dictionary design solves."""

# Answer :
"""
A  dictionary is faster and easier to use for finding a dish price because we can use the dish name as a key. In a list of tuples, we have to search 
for the dish in the list. This make it less easy to find a particular dish. A dictionary solves this problem because we can directly find the dish using its name.

"""

# SCENARIO 3 
# You are writing a delivery fee calculator that applies three different fee rules: no charge if the order value is Rs 500 or more, Rs 30 fee if distance is 5 km or 
# less, and Rs 60 fee for distances above 5 km. A colleague proposes writing this as a single lambda function.

"""Question: Explain why a named function defined with def is more appropriate than a lambda for this multi-condition fee logic. Then describe one specific situation 
inside this same app where a lambda would genuinely be the better choice."""

# Answer:
"""
A named function defined with def is more appropriate for this multi-condition fee logic because it allows for better readability and maintainability. The logic involves 
multiple conditions, which can make a lambda function complex and hard to understand. A named function can have a descriptive name and can include comments, making it easier 
for other developers to follow the logic.
"""

# SCENARIO 4 
# You are working on an order history feature that must save completed delivery orders to a JSON file so the system can reload all orders when the app restarts.

"""Question: Describe the complete Python sequence to write a single order dictionary to a JSON file and read it back. What exception is raised if the file does not exist at 
read time, and how should your program handle it so the app starts cleanly on its first run? """

# Answer :
"""
To write a single order dictionary to a JSON file, we can use the json module. First, we would import the json module, then open a file in write mode and use json.dump() to write the dictionary to the file. To read it back, 
we would open the file in read mode and use json.load() to load the data into a dictionary. If the file does not exist at read time, a FileNotFoundError exception is raised. We can handle this by using a try-except block to 
catch the exception and initialize an empty list or dictionary for orders, allowing the app to start cleanly on its first run.
"""

# SCENARIO 5 
# You are designing a delivery tracking system. Each delivery must store the rider's name, current GPS location, assigned order ID, and status (e.g. 'On the way'). It must also
# support actions such as updating the location and marking the delivery as complete.

"""Question: Justify why a class is a better design choice here than storing all of this data in separate variables or a plain dictionary. Identify at least two OOP principles your 
class design would apply and explain what each one achieves.  """

# Answer :
""" 
A class is a better design choice because it encapsulates all the data and methods related to a delivery into a single unit. This makes the code more organized, maintainable, and easier to understand. The two OOP principles that apply are:

1. Encapsulation: This principle involves bundling the data (rider's name, location, order ID, status) and methods (updating location, marking as complete) together within the class. It helps in hiding the internal details of the object and exposing only what is necessary.

2. Abstraction: This principle allows us to simplify complex systems by focusing on the essential features and hiding the unnecessary details. In this case, we can create simple methods to update the location or mark the delivery as complete without needing to know the internal implementation details.
"""


# SCENARIO 6 
# You are debugging a delivery cost calculator. When a user types 'two hundred' instead of a number for the order amount, the program crashes with an unhandled exception.

"""Question: Describe how you would use a try-except block to handle this error gracefully. Name the specific exception type you would catch, and explain how you would structure the code so
the program asks the user to re-enter the value instead of terminating.  """

# Answer :
"""
I would use a try-except block to catch the ValueError exception that occurs when trying to convert a non-numeric string to a float or int. Inside the try block, I would attempt to convert the 
user input to a number. If a ValueError is raised, the except block would catch it and prompt the user to re-enter the value. I would use a loop to keep asking for input until a valid number is 
provided, ensuring that the program does not terminate unexpectedly.
"""

