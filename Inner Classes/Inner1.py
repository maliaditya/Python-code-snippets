class Mobile:
    def __init__(self):
        print("Mobile constructor")

    class App:
        def __init__(self):
            print("App constructor")

        def appName(self):
            print("Instagram")


Mobile().App().appName()