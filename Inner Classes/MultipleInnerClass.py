class BCCI:

    def __init__(self):
        print("INDIAN CRICKET TEAM")

    class Ranji:

        def selection(self):
            print("from ranji")

    class IPL:

        def selection(self):
            print("from IPL")
        
BCCI().Ranji().selection()
BCCI().IPL().selection()