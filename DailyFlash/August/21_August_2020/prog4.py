permanant_members_of_un = ('UK','US','France','China','Russia','US','UK')
repeated_countries=set(x for x in permanant_members_of_un if permanant_members_of_un.count(x)==2)
print(tuple(repeated_countries))