from abc import ABC, abstractmethod

class Country(ABC):
    
    def __init__(self, land, population, continent, currency):
        self.land = land
        self.population = population
        self.continent = continent
        self.currency = currency

    def __del__(self):
        print("destructor")

    @abstractmethod
    def defence(self):
        pass

    @abstractmethod
    def primeMinster(self):
        pass


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

    def defence(self):
        print("4th powerful contry in the world")

    def primeMinster(self):
        print("Narendra Modi")


obj = India("Hindi","3,287,263 square kilometres", "1.3 billion", "Asia", "Rupee")
obj.country()
obj.defence()
help(object)