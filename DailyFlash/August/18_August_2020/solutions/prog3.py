allplayers = ["Kapil", "Kholi", "Raina", "Chahal", "Dhoni","Pant", "Dravid","Bumrah", "Harbhajan"]
currentTeam = ["Kholi", "Chahal", "Pant", "Bumrah"]
allplayers.reverse()
retired = [ x for x in allplayers if x not in currentTeam]
print(retired)