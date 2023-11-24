import  functools

# reduce()函数也是Python内置的一个高阶函数。

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

# ejemplo de reduce con el anterior list 

response = functools.reduce( lambda x, y : x + y['price'], items, 0 )

print( response )