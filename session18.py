# tsask : 1   Use re.findall() to extract all valid Indian phone numbers (10 digits, starting with 7, 8, or 9) from a given text 
#             string that contains random numbers, prices, and phone numbers like those seen in OLX or WhatsApp chats.
"""
import re

text = " contact me 9834562827. price is 6780 and number is 45321678"

numbers = re.findall(r'\b[789]\d{9}\b',text)
print(numbers)
"""

# task : 2  Write a Python function using re.search() that checks if a given string contains a valid date in the format 
#           DD/MM/YYYY (e.g., 25/06/2024), and returns True if found, otherwise False.<br><br><em><strong>Hint:</strong> 
#           Use the pattern '\b\d{2}/\d{2}/\d{4}\b'.</em>
"""
import re 

def check_date(text):
    pattern = r'\b\d{2}/\d{4}\b'

    if re.search(pattern,text):
        return True
    else:
        return False

print(check_date("My birthday is 27/07/2006"))
print(check_date("Today is a good day"))
"""

# task : 3 Given a messy text copied from a Zomato review containing multiple emails, use re.findall() to extract all 
#          valid email addresses and print them as a list.
"""
import re 

text = " Great food! contact rohit123@gmail.com or virat345@gmail.com for feedback."

emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b',text)
print(emails)
"""

# task : 4  Use re.sub() to mask all but the last 4 digits of any phone number in a string (e.g., replace 9876543210 with 
#           ******3210) like Paytm does for privacy.<br><br><em><strong>Constraint:</strong> Do not use loops; achieve this 
#           only with re.sub().</em>
"""
import re

text = " my phone number is 9876453324"

m = re.sub(r'\d(?=\d{4})','*',text)
print(m)
"""
# tsask : 5  Use ChatGPT to generate a regex pattern that matches Flipkart-style order IDs (e.g., OD123456789012345000) and test 
#            it in Python using re.search() on sample order strings.
"""
import re 

def check_order_id(order_id):
    patter = r'^OD\d{18}$'

    if re.search(patter,order_id):
        return True
    else:
        return False

print(check_order_id("OD123456789012345000"))
print(check_order_id("AB123456789012345000"))
"""
