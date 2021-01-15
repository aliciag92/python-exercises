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
    # Grand total of balances for all users
    # Average balance per user
    # User with the lowest balance
    # User with the highest balance
    # Most common favorite fruit
    # Least most common favorite fruit
    # Total number of unread messages for all users