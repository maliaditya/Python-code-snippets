import random
dice = [1,2,3,4,5,6]
playerlist=[]

no_of_players = int(input("Enter no of players (max 4): "))
if no_of_players <=4:
    for a in range(1,no_of_players+1):
        playerlist.append( input("Enter the name player{}: ".format(a)))
    while True:
        n = input("Press 'enter' to roll the dice. or 'x' to exit:" )
        if n == 'x':
            break
        print("-> ",random.choice(dice))
else:
    print("Max Limit exceded.")

