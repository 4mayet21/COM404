def is_league_united(hero1,hero2): 
    if ((hero1 == "Superman" and hero2 == "Wonder Woman") or (hero1 == "Wonder Woman" and hero2 == "Superman")):
        return True
    else:
        return False


def decide_plan(hero1, hero2):
    if is_league_united(hero1,hero2) == True:
        return "Time to save the world"
    else:
        return "We must unit the league!"

decide_plan("Superman", "Wonder Woman")

def run():
    hero1 = input("Enter the name of your first Hero: ")
    hero2 = input("Enter the name of your Second Hero: ")

    LorP = input("please enter \"league\" or \"plan\": ")
    if LorP == "league":
        print(str(is_league_united(hero1, hero2)))
    elif LorP == "plan":
        print(str(decide_plan(hero1, hero2)))
    else:
        print("invalid code please try again")

run()
    

