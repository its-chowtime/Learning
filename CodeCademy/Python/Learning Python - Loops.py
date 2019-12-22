#   Learn Python: Loops - Lesson 05
#   1 Introduction
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
for breed in dog_breeds:
  print(breed)

#   2 Create a For Loop
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
	print(game)
  
for sport in sport_games:
  print(sport)

#   Using Range in Loops
#   Allows us to print the same thing multiple times
promise = "I will not chew gum in class"

for x in range(5):
  print(promise)

#   Infinite Loops  
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  #students_period_A.append(student)
  students_period_B.append(student)
  print(student)

#   Break
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'

for x in dog_breeds_available_for_adoption:
  print(x)
  if x == dog_breed_I_want:
  	print("They have the dog I want!")
  	break

#   Continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)

#   While Loops using pop and append to add students into a limited list
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)

print(students_in_poetry)

#   Nested Loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  print(location)
  for x in location:
    scoops_sold += x
  print(scoops_sold)

#   List Comprehensions
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
#  why do we do [x for x in heights]
can_ride_coaster = [x for x in heights if x > 161]
print(can_ride_coaster)

#   More List Comprehensions
celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp*(9/5) + 32 for temp in celsius]

print(fahrenheit)

#   Review
single_digits = [0,1,2,3,4,5,6,7,8,9]
squares = []

for x in single_digits:
  squares.append(x**2)
  print(x) 
print(squares)

cubes = [x**3 for x in single_digits]
print(cubes)

#   Carly's Clipper Project
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price += price
average_price = total_price / len(prices)
print("Average Haircut Price: ${0}".format(average_price))

new_prices = [
  price - 5 #  what happens when we do prices vs price?
  for price in prices
]
print(new_prices)
      
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: ${0}".format(total_revenue))

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue ${0}".format(average_daily_revenue))

cuts_under_30 = [
  # expression
  hairstyles[i]
  # for statement
  for i in range(len(hairstyles))
  #	conditional
	if new_prices[i] < 30
]
print(cuts_under_30)

#   QUIZ

#   skips 2
numbers = [1, 1, 2, 3]
for number in numbers:
  if number % 2 == 0:
    continue
  print(number)

#   print 5 three times
for i in range(3):
  print(5)

#   stops code after printing two 1 / when it reaches %2 == 0
numbers = [1, 1, 2, 3]
for number in numbers:
  if number % 2 == 0:
    break
  print(number)

#   prints numbers up to range. Outputs = 0 1 2
for i in range(3):
  print(i)

#   comprehension list output 
#   desired_list = [-1, 0, 1, 2, 3]
[i-1 for i in range(5)]

#   create a list equal to desired_list = [10, 8, 20]
my_list = [5, 10, -2, 8, 20]
[i for i in my_list if i > 5]

#   Loop prints hello! for each of the 4 numbers, and does not print the number itself
numbers = [2, 4, 6, 8]
for number in numbers:
  print("hello!")