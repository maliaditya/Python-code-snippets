actors = {'Hemsworth':'Australian','Jackman':'Australian','Holland':'British',
            'Hiddleston':'British','Cumberbatch':'Britsh','Evans':'American','RDJ':'American'}

marvel = {'Zoe':'F','Hemsworth':'M','Evans':'M','Holland':'M','Paltrow':'F','Jackman':'M',
            'Hiddleston':'M','Cumberbatch':'M'}

nonAmericanMarvelActors = {x for x in marvel if marvel[x] == 'M' and actors[x]!='American'}

print(nonAmericanMarvelActors)
