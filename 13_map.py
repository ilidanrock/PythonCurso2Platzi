numbers = [1, 2, 3, 4, 5]
doubled = [number * 2 for number in numbers]
print(doubled)

# map() function

def double(x):
    return x * 2

doubled = map(double, numbers)

print(list(doubled))

# map() with lambda

doubled = map(lambda x: x * 2, numbers)

print(list(doubled))

