class Facebook:
    
    def create_post(self):
        print("Post Anything")

    def post_video(self):
        print("Post Any video")

class Instagram(Facebook):
    
    def post_video(self):
        print("Post Any video")
        print("Post Reels")


Instagram().post_video()