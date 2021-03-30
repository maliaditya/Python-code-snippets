


def Corona(city):
    def guidelines():
        city()
        print("Stirct curfew at night")
        print("Wear mask compulsory")
        print("Wash hands reularly")
        print("use sanitizers")
    return guidelines

@Corona
def city1():
    print("GUIDELINES FOR PUNE CITY")


@Corona
def city():
    print("GUIDELINES FOR NASHIK CITY")

city()