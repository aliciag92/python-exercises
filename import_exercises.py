#1. Import and test 3 of the functions from your functions exercise file.
    #Import each function in a different way:
        #import the module and refer to the function with the . syntax
import function_exercises

function_exercises.apply_discount(40, .50) #20.0

        #use from to import the function directly
from function_exercises import word

word("banana") #'Banana

        #use from and give the function a different name
from function_exercises import calculate_tip as ct

ct(.15, 63.50) #9.525


#For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
import itertools
    #1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools as it

len(list(it.product([1, 2, 3], 'abc'))) #9
    #2. How many different ways can you combine two of the letters from "abcd"?
len(list(it.combinations('abcd', 2))) #6

#Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
import json
profiles = json.load(open('profiles.json'))
    # Total number of users
len(profiles) #19
    # Number of active users
len([profile for profile in profiles if profile['isActive']]) #9
    # Number of inactive users
len([profile for profile in profiles if not profile['isActive']]) #10
        #or count = 0
        #   for user in profiles:
        #       if user['isActive'] == True:
        #           count = count + 1
        #   print(count)cs
        #or
        # len([profile for profile in profiles if profile['isActive'] == False])
    # Grand total of balances for all users
def convert_balances(balances):
    balances_float = []
    
    for balance in balances:
        balance = balance.replace("$", "")
        balance = balance.replace(",", "")
        
        balances_float.append(float(balance))
    
    return balances_float

balance = convert_balances([profile["balance"] for profile in profiles])
total_balance = sum(balance)

print(total_balance) #52667.02
    # Average balance per user
average_balance = total_balance / len(profiles)

round(average_balance, 2) #2771.95
    # User with the lowest balance
def convert_balances(balances):
    balances_float = []
    
    for balance in balances:
        balance = balance.replace("$", "")
        balance = balance.replace(",", "")
        
        balances_float.append(float(balance))
    
    return balances_float

balance = convert_balances([profile["balance"] for profile in profiles])
lowest_balance = min(balance)

print(lowest_balance) #1214.1
    # User with the highest balance
def convert_balances(balances):
    balances_float = []
    
    for balance in balances:
        balance = balance.replace("$", "")
        balance = balance.replace(",", "")
        
        balances_float.append(float(balance))
    
    return balances_float

balance = convert_balances([profile["balance"] for profile in profiles])
highest_balance = max(balance)

print(highest_balance) #3919.64
    # Most common favorite fruit
import statistics

statistics.mode(profile["favoriteFruit"] for profile in profiles) #'strawberry
    # Least most common favorite fruit
min(profile["favoriteFruit"] for profile in profiles) #'apple'
    # Total number of unread messages for all users
greetings = [profile["greeting"] for profile in profiles]
unread_messages = []

for greeting in greetings:
    for word in greeting:
        if word.isnumeric():
            unread_messages.append(int(word))

total_unread_messages = sum(unread_messages)
print(total_unread_messages) #111