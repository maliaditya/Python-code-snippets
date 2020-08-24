meals = {'Panner':'Veg','Mutton Korma':'Non-Veg','Chicken malai':'Non-Veg','Tandoori roti':'Veg','Drumsticks':'Non Veg'}

weekday =int(input("enter weekday: "))

if weekday %2 != 0:
    print("My friend can eat ",len(meals)," dishes.")
else:
    count =0
    for a in meals:
        if meals[a] == 'Veg':
            count +=  1

    print("My friend can eat ",count)," dishes."