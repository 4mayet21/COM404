# get sight and sound from user
print("what did I hear?")
sound = str(input())
print("what did I see")
sight = str(input())

#print resopnse
if ((sound == "grrr") and (sight == "two red eyes")):
    print("There is a scary creature. I should get out of here!")
elif((sound == "No, No, No") and (sight == "A visage too monstrous and chilling to describe")):
    print("Oh, no. Margaret Thatcher has risen from her grave! I should get out of here!")
else:
    print("I am a little scared but I will continue.")
