def escape_by(plan):
    if plan == "jumping over":
        print("Might as well jump! Go ahead and jump!")
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("But you! Why you wanna give me a run-around? " 
        "Is it a sure-fire way to speed things up? " 
        "When all it does is slow me down")
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "going deeper":
        print("Deeper and deeper, and deeper, and deeper")
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

escape_by('going deeper')