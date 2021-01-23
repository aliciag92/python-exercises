Exercise Solutions
You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

In [1]:
# Name of the Game
# Convert English into Python
little_mermaid_days = 3 # Variables hold nouns
brother_bear_days = 5 # If you have a noun or a noun phrase
hercules_days = 1
price_per_movie = 3
total = little_mermaid_days * price_per_movie + brother_bear_days * price_per_movie + hercules_days * price_per_movie
total
Out[1]:
27
Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

In [2]:
google_rate = 400
amazon_rate = 380
facebook_rate = 350
facebook_hours = 10
google_hours = 6
amazon_hours = 4
amazon_subtotal = amazon_hours * amazon_rate
google_subtotal = google_hours * google_rate
facebook_subtotal = facebook_hours * facebook_rate
total = amazon_subtotal + google_subtotal + facebook_subtotal
f"${total} is the total of consulting with these companies"
Out[2]:
'$7420 is the total of consulting with these companies'
A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

In [3]:
class_has_space = True
schedule_works = True
can_be_enrolled = class_has_space and schedule_works
can_be_enrolled
Out[3]:
True
In [4]:
class_has_space = True
schedule_conficts = False # This is the same as saying the schedule works
can_be_enrolled = class_has_space and not schedule_conficts # not schedule_conflicts == schedule_works
can_be_enrolled
Out[4]:
True
A product offer can be applied only if people buys more than 2 items, and the offer has not expired.

Premium members do not need to buy a specific amount of products.

In [5]:
is_premium_member = False
purchasing_more_than_two_items = False
offer_valid = True

offer_can_be_applied = offer_valid and (is_premium_member or purchasing_more_than_two_items)
offer_can_be_applied
Out[5]:
False
Use the following code to follow the instructions below:

username = 'codeup'

password = 'notastrongpassword'

Create a variable that holds a boolean value for each of the following conditions:

the password must be at least 5 characters
the username must be no more than 20 characters
the password must not be the same as the username
bonus neither the username or password can start or end with whitespace
In [6]:
username = "codeup"
password = "notastrongpassword"
In [7]:
password_is_at_least_5_characters = len(password) >= 5
In [8]:
username_less_than_twenty_characters = len(username) <= 20
In [9]:
password_different_than_username = username != password
In [10]:
x = "   howdy "
x.strip()
Out[10]:
'howdy'
In [11]:
password_has_no_beginning_or_ending_whitespace = password == password.strip()
In [12]:
username_has_no_beginning_or_ending_whitespace = username == username.strip()
In [13]:
is_valid_username_and_password = (password_is_at_least_5_characters 
                              and username_less_than_twenty_characters
                              and password_different_than_username
                              and password_has_no_beginning_or_ending_whitespace
                              and username_has_no_beginning_or_ending_whitespace)

is_valid_username_and_password
Out[13]:
True
In [14]:
# (operand operator operand) or (operand operator operand) and ...