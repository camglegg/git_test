# This program says "Hello" and asks for my name.

print("Hello World!")
# Changed this to assign the variable while simultaneously asking for the input.
my_name = input("What is your name? ")
print('It is nice to meet you, ' + my_name)
print('The length of your name is : ')
print(len(my_name))
my_age = input('What is your age? ')
# This needs the "str" and "int" or it breaks.
print('You will be ' + str(int(my_age)+1) + ' in a year.')

