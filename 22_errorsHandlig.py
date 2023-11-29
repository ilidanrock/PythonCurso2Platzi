
try:
     print(0/ 0)
except ZeroDivisionError as error:
    print("You can't divide by zero", error)


try:
    assert 1 != 1, "1 is not equal to 1 "
except AssertionError as error:
    print(error)


