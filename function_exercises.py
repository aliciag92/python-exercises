#1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(n):
    return n == 2 or n == '2'

is_two(2) #True
is_two('2') #True
is_two(5) #False
is_two('five') #False


#2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(string):
    return string in ["a", "e", "i", "o", "u"]

is_vowel("a") #True
is_vowel("b") #False
is_vowel("aa") #False

#3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(string):
    return string not in ["a", "e", "i", "o", "u"]

is_consonant("b") #True
is_consonant("e") #False

    #alternate for exc 3:
def is_consonant(letter):
    return is_vowel(letter) != True

is_consonant('d') #True
is_consonant('e') #False

#4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def word(string):
    return string.capitalize()

word("banana") #'Banana'
word("hello") #'Hello'
word("i hope i am doing this right?") #'I hope i am doing this right?'

#5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip_percent, total_bill):
    return tip_percent * total_bill

calculate_tip(.20, 100) #20.0
calculate_tip(.20, 13.72) #2.744
calculate_tip(.15, 63.50) #9.525

#6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(og_price, disc_percentage):
    return (og_price) - (og_price * disc_percentage)

apply_discount(40, .50) #20.0
apply_discount(100, .35) #65.0
apply_discount(15, .10) #13.5

#7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(number):
    return int(number.replace(',', ''))
                    #syntax: .replace takes two arguments ('what to replace', 'what you're replacing it with)

handle_commas("1,000") #1000
handle_commas("1,234") #1234

#8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(number_grade):
    if number_grade >= 90:
        return "A"
    elif number_grade >= 80:
        return "B"
    elif number_grade >= 70:
        return "C"
    elif number_grade >= 60:
        return "D"
    else:
        return "F"

get_letter_grade(70) #'C'
get_letter_grade(68) #'D'
get_letter_grade(88) #'B'
get_letter_grade(55) #'F'
get_letter_grade(100) #'A'

#9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    for char in "aeiouAEIOU":
        string = string.replace(char, "")
    return string

remove_vowels('ABCDEabcde') #'BCDbcd'
remove_vowels('Super Mario SUNSHINE') #'Spr Mr SNSHN'

#10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    # anything that is not a valid python identifier should be removed
    # leading and trailing whitespace should be removed
    # everything should be lowercase
    # spaces should be replaced with underscores
    # for example:
        #   Name will become name
        #   First Name will become first_name
        #   % Completed will become completed
def normalize_name(string):
    return string.lower().replace(" ", "_")

normalize_name("Alicia Gonzalez") #'alicia_gonzalez

#11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
    # cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    # cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(numlist):
    return [sum(numlist[0:x:1]) for x in range(len(numlist)+1)][1:]

cumulative_sum([1, 2, 3]) #[1, 3, 6]

##Additional Exercise
# Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

##Bonus
#1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
def twelveto24(string)

#2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
    # col_index('A') returns 1
    # col_index('B') returns 2
    # col_index('AA') returns 27
def col_index(colname)