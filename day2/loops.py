names = ['Florin', 'Pablo', 'Monika'] 

## Brackets are important!
# [] are for lists
# {} are for dictionaries
# () are for tuples

#for name in names:
#    print(name)

#for name in names:
#    print(name.upper())

prices = [123, 456, 112]

vat_rate = 0.21
for price in prices:
    price_with_vat = round(price*(1+vat_rate),2)
    if price_with_vat > 500:
        print("Expense policy violation")
    else:
        print(f'The price with VAT is {price_with_vat}')
