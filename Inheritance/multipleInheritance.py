class Facebook:
    def __init__(self):
            print("Founder Zukerberg")

    def chatting(self):
        print("Chat with friends")

    def sharePics(self):
        print("Post Images")


class Tiktok:

    def create(self):
        print("Create faltu videos")



class Instagram(Facebook, Tiktok):

    def Reels(self):
        print("Post your Reels")




obj = Instagram()
obj.chatting()
obj.create()