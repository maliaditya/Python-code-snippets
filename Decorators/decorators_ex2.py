def cricket(func):
    def wrapper_func():
        print("Play Toss before {} ".format(func.__name__))
        return func()
    return wrapper_func


@cricket
def start_cricket():
    print("Team python has won the toss and had choosen to Bat")


start_cricket()