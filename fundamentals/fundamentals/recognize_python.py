num1 = 42       # variable declaration, numbers, int
num2 = 2.3      # variable declaration, numbers, float
boolean = True      # variable declaration, Boolean
string = 'Hello World' # variable declaration, strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']      # variable declaration, dictionary, array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}      # variable declaration, list
fruit = ('blueberry', 'strawberry', 'banana')       #variable declaration, tuples
print(type(fruit))      # function, return, type check
print(pizza_toppings[1])        # function, return, dictionary, change value
pizza_toppings.append('Mushrooms')      # function, dictionary, add value
print(person['name'])       # function, return
person['name'] = 'George'       # variable declaration, strings
person['eye_color'] = 'blue'        # variable declaration, strings
print(fruit[2])         # function, return, dictionary, change value

if num1 > 45:       # conditional, if
    print("It's greater")       # function, return, strings
else:       #conditional, else
    print("It's lower")         # function, return, strings

if len(string) < 5:         # conditional, if
    print("It's a short word!")         # function, return, strings
elif len(string) > 15:      #conditional, else if
    print("It's a long word!")          # function, return, strings
else:       # conditional, else
    print("Just right!")        # function, return, strings

for x in range(5):      # for loop, start
    print(x)        # function, return, stop
for x in range(2,5):        # for loop, start
    print(x)        # function, return, stop
for x in range(2,10,3):         # for loop, start
    print(x)        # function, return, stop
x = 0       # variable declaration, numbers, int
while(x < 5):       # while, start
    print(x)        # function, return, stop
    x += 1          # variable declaration, numbers, int, add value

pizza_toppings.pop()        # function, add value
pizza_toppings.pop(1)       # function, access value

print(person)       # function, return
person.pop('eye_color')     # function, add value, strings
print(person)       # function, return

for topping in pizza_toppings:      # for loop, start
    if topping == 'Pepperoni':      # conditional, if, strings
        continue        # for loop, continue
    print('After 1st if statement')     # function, return, stop, strings
    if topping == 'Olives':         # conditional, if, strings
        break       # for loop, break

def print_hello_ten_times():        #function, start
    for num in range(10):       # for loop, start
        print('Hello')      # function, return, stop, strings

print_hello_ten_times()     # function, return

def print_hello_x_times(x):         #function, start
    for num in range(x):        # for loop, start
        print('Hello')      # function, return, stop, strings

print_hello_x_times(4)      # function, return

def print_hello_x_or_ten_times(x = 10):     #function, start
    for num in range(x):        # for loop, start
        print('Hello')      # function, return, stop, strings

print_hello_x_or_ten_times()        # function, return
print_hello_x_or_ten_times(4)       # function, return


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)