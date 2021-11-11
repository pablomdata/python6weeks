name = input("Write your name please: ")
country = input("What is your country? ")
age = input("How old are you? ")

# Calculate days lived from age
days_lived = int(age)*365.25 # Forcing age to be treated as an integer(type coercion)

# Conditional Logic: Change the values of greeting according to the country
if country == 'Czechia':
    greeting = 'Ahoj'

elif country == 'Romania':
    greeting = 'Salut'   

elif country == 'Mexico' or country == 'Spain':
    greeting = 'Hola'

else:
    greeting = 'Hello'


# Make an exception for Florin
if country == 'Romania' and name == 'Florin':
    greeting = 'Bonjour'

# If message gets too long, we can use f-strings
message = f'{greeting} {name}!. You are {age} years old. You have lived {days_lived} days.'

print(message)