def box(word):
  print("*" * (len(word)+4))
  print("*", word, "*")
  print("*" * (len(word)+4))
  
def uppercase(word):
    print(word.upper())

def lowercase(word):
    print(word.lower())

def mirror(word):
    scrawl = word
    revMod = ""
    for item in range(0, len(scrawl)):
        rev = scrawl[item]
        revMod = rev + revMod
        
    print(revMod)

def repeat(word):
    rep = int(input("how many times: "))
    for x in range(0, rep):
        print(word)



def CrypticWord():
  word = input("Please enter your Cryptic Word:  ")
  display = input("would you like a box, uppercase, lowercase, mirrored or repeated?  ")
  if display == 'box':box(word)
  elif display == 'uppercase':    uppercase(word)
  elif display == 'lowercase':   lowercase(word)
  elif display == 'mirrored':  mirror(word)
  elif display == 'repeated':  repeat(word)
 # elif 
#repeat = input("how many times would you like this repeated?  ")

CrypticWord()