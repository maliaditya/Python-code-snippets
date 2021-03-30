def TeamIndia(record):
    def Selection():
        print("player for team India")
        record()
        print("New player for team India")

    return Selection


def stateplayer(record):
    def Selection():
        print("Player from rangi or IPL")
        record()
        print("State level player selected")
    return Selection


@TeamIndia
@stateplayer
def playerselection():
    print("BCCI WATCHING")

playerselection()