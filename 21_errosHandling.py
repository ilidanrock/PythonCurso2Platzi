
# code error handling example 1

try:

    print(1/0)

except ZeroDivisionError:

    print("You can't divide by zero")

# code error handling example 2 different to example :

age = int(input("How old are you? "))

if age < 18 :
    raise Exception("You are too young to drive a car")