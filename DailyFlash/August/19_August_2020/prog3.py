marvel = ['Robert Downey Jr','Chris Hemsworth','Scarlett Johansson','Ryan Reynolds']
dc = ['Gal Gadot','Henry Cavil','Ezra Miller','Ryan Reynolds']

newmarvel= [x for x in marvel if x not in dc]
newDC = [x for x in dc if x not in marvel ]

li = newDC+newmarvel

set = {x for x in li }
print(set)