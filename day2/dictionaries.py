products = {
    'history':['History of the Roman Empire', 'Egyptian Pyramids', 'Aztecs'],
    'science':['Physics if Fun', 'Planets', 'Computer History'],
    'cooking':['Romanian Cuisine','Pizza Book', 'Mexican Cuisine'],
}

#print(products['history'][-1])

products = {
    'history':{'History of the Roman Empire':100, 'Egyptian Pyramids':150, 'Aztecs':100},
    }

print(products['history']['Aztecs'])