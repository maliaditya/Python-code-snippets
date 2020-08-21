food_at_wedding = (('Indian','Friters','Curry'),('Chinese','Chopsy','Noodles'),('American','Fries','Wraps'))

food_type = tuple(i for i,j,k in food_at_wedding )
starters = tuple(j for i,j,k in food_at_wedding)
main_course = tuple(k for i,j,k in food_at_wedding)

print(food_type)
print(starters)
print(main_course)