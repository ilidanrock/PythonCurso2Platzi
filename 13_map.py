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

# Path: 14_filter.py

numbers = [1, 2, 3, 4, 5]

def is_even(x):
    return x % 2 == 0

even = filter(is_even, numbers)

print(list(even))

items = [
    {
        'product': 'Rice',
        'price': 10,
        'quantity': 5
    },
    {
        'product': 'Wheat',
        'price': 20,
        'quantity': 10
    },
    {
        'product': 'Sugar',
        'price': 30,
        'quantity': 15
    }
]

prices = map( lambda x : x['price'], items )

new_items = list(map(lambda item: {**item, "fee_with_fee": item['price'] * 0.16}, items))

print( list(prices))

print( new_items )

print(items)