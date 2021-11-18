numbers = [1,2,3,4,5,6]

def square(number=0):
    sq = number**2
    return sq

for number in numbers:
    print(square(number))

print("The value without parameters is: ", square())

def dot_product(x,y):
    result = 0 # accumulator
    for i in range(len(x)): # i = counter
        result = result + x[i]*y[i]
    return result

dp = dot_product([1,0,0],[-1,1,0])    
print(dp)

# CHALLENGE!
def poly_eval(coeffs, x):
    '''
    Given list of coefficients: [1,3,2]
    value of x:
    Return 1+3*x+2*x**2
    '''
    pass

poly_eval([1,3,2],1)