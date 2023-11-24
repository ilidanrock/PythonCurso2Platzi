

# filter

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

prices = filter( lambda x : x['price'] > 10, items )

print( list(prices))

# list of dictionaries

items_2 = [
    { 'name': 'Rice', 'price': 10 },
    { 'name': 'Wheat', 'price': 20 },
    { 'name': 'Sugar', 'price': 30 }    
] 

