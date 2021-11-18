numbers = [1,2,3,4,5,6]

def square(number=0):
    sq = number**2
    return sq

squares = [number**2 for number in numbers]    
print(squares)

squares_less_than_4 = [number**2 for number in numbers if number<4]
print(squares_less_than_4)

squares_even = [number**2 if number%2==0 else 0 for number in numbers]
print(squares_even)

sum_squares = sum([number**2 for number in numbers])
print(sum_squares)

x = [-1,0,1]
y = [0,1,0]
dot_product = sum([x[i]*y[i] for i in range(len(x))])
print(dot_product)

names = ['Monika', 'Pablo', 'Florin']
capitalize_names = [name.upper() for name in names]
print(capitalize_names)
