class Facebook:
    
    def __init__(self):
        print("Founder Zukerberg")

    def chatting(self):
        print("Chat with friends")

    def sharePics(self):
        print("Post Images")

class Instagram(Facebook):

    def __init__(self):
        print("Parent Company Facebook")

    def Reels(self):
        print("Post your Reels")

    

obj = Instagram()
obj.chatting()
obj.sharePics()
obj.Reels()