
class Country:
    
    def __init__(self, land, population, continent, currency):
        self.land = land
        self.population = population
        self.continent = continent
        self.currency = currency

    def __del__(self):
        print("destructor")


class India(Country):
    
    def __init__(self,language,land, population, continent, currency):
        super().__init__(land, population, continent, currency)
        self.language = language


    def country(self):
        print("INDIA")
        print("LAND: "+ self.land)
        print("Population: "+ self.population)
        print("Continent: "+ self.continent)
        print("Currency: "+ self.currency)
        print("Language: "+ self.language)

    @classmethod
    def defence(self):
        print("4th powerful contry in the world")

    @classmethod
    def primeMinster(self):
        print("Narendra Modi")


class Pakistan(Country):
    
    def __init__(self,language,land, population, continent, currency):
        super().__init__(land, population, continent, currency)
        self.language = language


    def country(self):
        print("Pakistan")
        print("LAND: "+ self.land)
        print("Population: "+ self.population)
        print("Continent: "+ self.continent)
        print("Currency: "+ self.currency)
        print("Language: "+ self.language)




obj = India("Hindi","3,287,263 square kilometres", "1.3 billion", "Asia", "Rupee")
obj.country()
obj.defence()
obj.primeMinster()
del obj

print()

obj2 = Pakistan("Urdu","8.819 lakh km", "142.5 million", "Asia", "Rupee")
obj2.country()
obj2.defence()
obj2.primeMinster()

