menu = {
    'vegan':{'falafel':200, 'pasta':300},
    'kids':{'chicken':150, 'ketchup':150}
    }

print('The options on the menu are: ')
for option in menu:
    print(option)

chosen_menu = input('Which menu would you like? ')
chosen_menu = chosen_menu.lower() #Ensure that the input would be compatible with our data

if chosen_menu in menu.keys():
    print("The dishes available are: ")
    for dish in menu[chosen_menu]:
        print(dish)
    chosen_dish = input('Which dish would you like? ')
    chosen_dish = chosen_dish.lower()
    chosen_dish_price = menu[chosen_menu][chosen_dish]
    print(f"It will be {chosen_dish_price} Czech Crowns")

else:
    print("Invalid option. No service")


#print(menu['vegan'].keys())