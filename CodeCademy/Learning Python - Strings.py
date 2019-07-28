#   Learn Python: Strings - Lesson 06

#   Introduction
favorite_word = "boo"
print(favorite_word)

#   Strings can be thought of as a list of characters
my_name = "Patrick"
first_initial = my_name[0]
# Returns P

#   Slicing strings | generate a username and password using first 5 letters, then letters 3-6
first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6]

#   Concatenating Strings | Creating a new user account
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name
# This line threw me off
new_account = account_generator(first_name, last_name)

print(new_account)

#   Slicing Strings | using length of a string (len())
first_name = "Reiko"
last_name = "Matsuki"
def password_generator(first_name, last_name):
  password = first_name[-3:] + last_name[len(last_name)-3:] 
  return password
temp_password = password_generator("Reiko", "Matsuki")

print(temp_password)

#   Negative Indices | returns f and life
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]

#   Strings are Immutable | cannot change string once created | changes Bob to Rob
first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)

#   Escape Characters | Add \ in front of the special character, this will allow "" to be in the string
password = "theycallme\"crazy\"91"

#   Iterating through Strings | count the numbers in the string (like using len())
def get_length(x):
  count = 0
  for letter in x:
    count += 1
  return count
print(get_length("asdkal"))

#   Strings and Conditionals (part 1)
def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

# Below is my code. Is there a difference?
def letter_check(word, letter):
  for x in word:
    if x == letter:
      return True
    else:
      return False
    
print(letter_check("Apples","o"))

#   Strings and Conditionals (part 2) | using <letter in word> is a boolean expression
def contains(big_string, little_string):
  return little_string in big_string

# Looking for common letters and putting it into a new list (Had some trouble)
def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

#   Review | 1. Print first 3 and first 4 of First,Last | 2. Shift all letters | 3. Create a for loop to shift
# My code
def username_generator(first_name,last_name):
  username = first_name[:3] + last_name[:4]
  return username

def password_generator(username):
  password = username[-1] + username[:-1]
  for i in range(0,len(username)):
    
    new = x + username
    return new
  #return password
print(username_generator("oatpls","mealeas"))
print(password_generator("oatmeal"))

#   Quiz
def print_some_characters(word):
  for i in range(len(word)):
    if i % 2 == 0:
      print(word[i])

print_some_characters("watermelon")

# what is py in py least_favorite_fruit[5:8]