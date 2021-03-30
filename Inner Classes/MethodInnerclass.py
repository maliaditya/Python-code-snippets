def outer():

    class Inner:
        def test(self):
            print("Test")

    
    obj = Inner()
    obj.test()



outer()