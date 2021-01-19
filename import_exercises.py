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
                # ttl_users = len(profiles)
                # ttl_users 

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

            #def clean_balance(balance):
            #    balance = balance.replace(',', '')
            #    balance = balance.replace('$', '')
            #    return float(balance)
            #ttl_balances = sum([clean_balance(profile['balance']) for profile in profiles])
    
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
#or
        
# This variable will hold on to the user dict with the lowest balance
# we'll start of by saying the user with the lowest balance is the first user.
##user_with_lowest_balance = profiles[0]

# Now we can loop through the remaining profiles and compare the balances
##for profile in profiles[1:]:
    # if the current profile has a lower balance than our lowest balance so far,
    ##if clean_balance(profile['balance']) < clean_balance(user_with_lowest_balance['balance']):
        # set this profile as the user with the lowest balance
        ##user_with_lowest_balance = profile

##user_with_lowest_balance

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

# We'll use the same strategy as before, but with the highest balance this time
##user_with_highest_balance = profiles[0]

##for profile in profiles[1:]:
##    if clean_balance(profile['balance']) > clean_balance(user_with_highest_balance['balance']):
##        user_with_highest_balance = profile

##user_with_highest_balance

    # Most common favorite fruit
import statistics

statistics.mode(profile["favoriteFruit"] for profile in profiles) #'strawberry
    
    # Least most common favorite fruit
min(profile["favoriteFruit"] for profile in profiles) #'apple'

 # Our goal here is to transform the list above into a dictionary where the keys are the unique fruit names,
# and the values are the number of times that fruit appears in the list above.

# To do so, we'll start with an empty dictionary:
##fruit_counts = {}

# Now we can loop through the list of favorite fruits
##for fruit in favorite_fruits:
    # if the fruit name already exists as a key in the fruit_counts dictionary
##    if fruit in fruit_counts:
        # We already have started a acount for this fruit
        # add 1 to the number of times that fruit appears
##        fruit_counts[fruit] += 1
##    else:
        # We don't yet have an entry for this fruit
        # Create it and set it to 1
##        fruit_counts[fruit] = 1   
##fruit_counts ###{'strawberry': 9, 'apple': 4, 'banana': 6}

    # Total number of unread messages for all users
greetings = [profile["greeting"] for profile in profiles]
unread_messages = []

for greeting in greetings:
    for word in greeting:
        if word.isnumeric():
            unread_messages.append(int(word))

total_unread_messages = sum(unread_messages)
print(total_unread_messages) #111

#correct sol:
def extract_digits(s):
    return ''.join([c for c in s if c.isdigit()])

n_unread_messages = [int(extract_digits(profile['greeting'])) for profile in profiles]
# sum([int(message) for message in n_unread_messages])
sum(n_unread_messages) #210