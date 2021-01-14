#Exercises
#Do your work for this exercise in a file named control_structures_exercises.py.

#1. Conditional Basics
#1a. prompt the user for a day of the week, print out whether the day is Monday or not
day_of_the_week = input ("What is today?") #type today's day (wednesday)
print(day_of_the_week) #Wednesday

if day_of_the_week == 'Monday':
    print ('Today is Monday')
else:
    print('It is not Monday')

#another solution



#1b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Saturday', 'Sunday']

if day_of_the_week in weekday:
    print ("It is a weekday")
else: 
    print ("It is the weekend")

#another solution




#1c. create variables and make up values for
    #the number of hours worked in one week
    #the hourly rate
    #how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. 
#You get paid time and a half if you work more than 40 hours
number_of_hours_worked = 42
hourly_rate = 20
paycheck = number_of_hours_worked * hourly_rate
print(paycheck)

if number_of_hours_worked > 40:
    overtime_rate = hourly_rate * 1.5
    overtime_hours = number_of_hours_worked - 40
    weekly_pay = (40 * hourly_rate) + (overtime_rate * overtime_hours)
    print(weekly_pay)
else:
    weekly_pay = number_of_hours_worked * hourly_rate
    print(weekly_pay)

#another solution:



#2. Loop Basics
#2a. While
    #Create an integer variable i with a value of 5.
    i = 5
    #Create a while loop that runs so long as i is less than or equal to 15
    while i <= 15:
        print(i)
        i += 1

    #Each loop iteration, output the current value of i, then increment i by one.
    i = 5
    while i <= 15:
        print(i)
        i += 1

    #Your output should look like this:
        # 5
        # 6
        # 7
        # 8
        # 9
        # 10
        # 11
        # 12
        # 13
        # 14
        # 15

    #Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
    i = 0
    while i <= 100:
        print (i)
        i += 2

    #Alter your loop to count backwards by 5's from 100 to -10.
    i = 100
    while i >= -10:
        print (i)
        i -= 5

    #Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. 
    i = 2
    while i < 1000000:
        print (i)
        i **= 2 #or i = i ** 2 or i *= i
    #Output should equal:
        # 2
        # 4
        # 16
        # 256
        # 65536
    
    #Write a loop that uses print to create the output shown below.
    i = 100
    while i >= 5:
        print (i)
        i -= 5   
        # 100
        # 95
        # 90
        # 85
        # 80
        # 75
        # 70
        # 65
        # 60
        # 55
        # 50
        # 45
        # 40
        # 35
        # 30
        # 25
        # 20
        # 15
        # 10
        # 5

#2b. For Loops
    ##2bi. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
            #For example, if the user enters 7, your program should output:
        # 7 x 1 = 7
        # 7 x 2 = 14
        # 7 x 3 = 21
        # 7 x 4 = 28
        # 7 x 5 = 35
        # 7 x 6 = 42
        # 7 x 7 = 49
        # 7 x 8 = 56
        # 7 x 9 = 63
        # 7 x 10 = 70
    favorite_number = int(input("What is your favorite number?"))
    print(favorite_number)
    type(favorite_number) #double check that output is integer

    for number in range(1, 11):
        print(f' {favorite_number} x {number} = {number * favorite_number}')

    ##2bii. Create a for loop that uses print to create the output shown below.
    for number in range(1, 10):
        print (str(number) * number)   
        # 1
        # 22
        # 333
        # 4444
        # 55555
        # 666666
        # 7777777
        # 88888888
        # 999999999

#2c. break and continue
    ##2ci. Prompt the user for an odd number between 1 and 50. 
    # Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). 
    # Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
while True:
    user_number = input("Please enter an odd number between 1 and 50")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number % 2 == 0: # if it's even
            continue
        break

i = 1
while i <= 50:
    if i == user_number:
        print(f"Yikes! Skipping number: {i}")
        i += 2
        continue
    print(f"Here is an odd number: {i}")
    i += 2
            #Your output should look like this:
                # Number to skip is: 27

                # Here is an odd number: 1
                # Here is an odd number: 3
                # Here is an odd number: 5
                # Here is an odd number: 7
                # Here is an odd number: 9
                # Here is an odd number: 11
                # Here is an odd number: 13
                # Here is an odd number: 15
                # Here is an odd number: 17
                # Here is an odd number: 19
                # Here is an odd number: 21
                # Here is an odd number: 23
                # Here is an odd number: 25
                # Yikes! Skipping number: 27
                # Here is an odd number: 29
                # Here is an odd number: 31
                # Here is an odd number: 33
                # Here is an odd number: 35
                # Here is an odd number: 37
                # Here is an odd number: 39
                # Here is an odd number: 41
                # Here is an odd number: 43
                # Here is an odd number: 45
                # Here is an odd number: 47
                # Here is an odd number: 49

#Walkthrough:
#continuously
    # prompt the user for a positive number
    # Check if the input is composed of digits, if so
        # Convert to a numeric type
        # Check if the number is negative or 0, if so
        # Go back to square one
    # Stop the loop (break)


#2d. The input function can be used to prompt for input and use that input in your python code. 
    # Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
    # (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
# enter a positive number
while True:
    user_number = input("Please enter a positive number: ")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number <= 0:
            continue
        break

for i in range(0, user_number + 1):
    print(i)


#2e. Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.
# enter a positive number
while True:
    user_number = input("Please enter a positive number: ")
    if user_number.isdigit():
        user_number = int(user_number)
        if user_number <= 0:
            continue
        break

for i in range(user_number, 0, -1):     #list(range(10, 0, -1))
    print(i)


#3. Fizzbuzz
#One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
    #Write a program that prints the numbers from 1 to 100.
    #For multiples of three print "Fizz" instead of the number
    #For the multiples of five print "Buzz".
    #For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


#4. Display a table of powers.
    #Prompt the user to enter an integer.
    #Display a table of squares and cubes from 1 to the value entered.
    #Ask if the user wants to continue.
    #Assume that the user will enter valid data.
    #Only continue if the user agrees to.
user_input = int(input("Please enter an integer: "))

print()
print("number | squared | cubed")
print("------ | ------- | -----")
for i in range(1, user_input + 1):
    print("%6d | %7d | %5d" % (i, i**2, i**3))

    #Example Output
        #What number would you like to go up to? 5

        #Here is your table!

        #number | squared | cubed
        #------ | ------- | -----
        #1      | 1       | 1
        #2      | 4       | 8
        #3      | 9       | 27
        #4      | 16      | 64
        #5      | 25      | 125

#Bonus: Research python's format string specifiers to align the table



#5. Convert given number grades into letter grades.
    #Prompt the user for a numerical grade from 0 to 100.
    #Display the corresponding letter grade.
    #Prompt the user to continue.
    #Assume that the user will enter valid integers for the grades.
    #The application should only continue if the user agrees to.
    #Grade Ranges:
        #A : 100 - 88
        #B : 87 - 80
        #C : 79 - 67
        #D : 66 - 60
        #F : 59 - 0

numeric_grade = int(input("Please enter a number grade: "))

# convert to letter
if numeric_grade >= 88:
    print("A")
elif numeric_grade >= 80:
    print("B")
elif numeric_grade >= 67:
    print("C")
elif numeric_grade >= 60:
    print("D")
else:
    print("F")

#with while loop:
while True:
    # TODO: prompt user for this value
    numeric_grade = int(input("Please enter a number grade: "))

    # convert to letter
    if numeric_grade >= 88:
        print("A")
    elif numeric_grade >= 80:
        print("B")
    elif numeric_grade >= 67:
        print("C")
    elif numeric_grade >= 60:
        print("D")
    else:
        print("F")
    
    wants_to_continue = input("Do you want to continue? ")
    if not wants_to_continue.lower().startswith("y"):
        break

#Bonus
#Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

#6. Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
#6a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
# consider that this data structure could represent rows from a
# database table
books = [
    {"title": "This is where I leave you", "author": "Jonathan Tropper", "genre": "Adult Fiction"},
    {'title': 'Parable of the Sower', 'author': 'Octavia E. Butler', 'genre': 'Science Fiction'},
    {"title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction"},
    {'title': 'The Singularity is Near', 'author': 'Ray Kurzweil', 'genre': 'Artificial intelligence/Technology'},
    {"title": "Star Wars: The Old Republic - Revan", "author": "Sean Williams", "genre": "Science Fiction"},
]

selected_genre = input("Please enter a genre: ")
selected_books = [book for book in books if book['genre'] == selected_genre]

# for singular in plural
# plural variable names indicate a list of things
# the singular version is one thing from the list
for book in selected_books:
    print("---")
    # print("title: {}".format(book['title']))
    # print("author: {}".format(book['author']))
    # print("genre: {}".format(book['genre']))
    
    # other ways to do it
    print("Title: %s" % book['title'])
    print("Author: " + book['author'])
    print(f"Genre: {book['genre']}")