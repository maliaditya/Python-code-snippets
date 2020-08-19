legacy = {7:"CSK",3:"CSK",13:"CSK",45:"MI",33:"MI",99:"MI",77:"DC",41:"DC",19:"DC"}

csk = {x for x in legacy if legacy[x]=="CSK"}
mi = {x for x in legacy if legacy[x]=="MI"}
dc = {x for x in legacy if legacy[x]=="DC"}

print(csk)
print(mi)
print(dc)
