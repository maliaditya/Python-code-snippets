class AttrError:
    pass

try:
    AttrError().fun()
except AttributeError as e:
    print(e)
