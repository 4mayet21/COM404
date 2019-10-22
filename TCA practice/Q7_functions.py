def under(word):
    print(word)
    line = ""
    for num in range(0,len(word)):
        line = line + "*"
    print(line)

def over(word):
    line = ""
    for num in range(0,len(word)):
        line = line + "*"
    print(line)
    print(word)

def both(word):
    line = ""
    for num in range(0,len(word)):
        line = line + "*"
    print(line)
    print(word)
    print(line)


def grid(word, size):
    WordLine = ""
    Line = ""
    
    LineLong = ""
    for num1 in range(0,len(word)):
        Line = Line + "*"
    
    for num2 in range(0,size):
        LineLong = LineLong + Line +"   "
        if num2 == size -1:
            WordLine = WordLine + word
        else:
            WordLine = WordLine + word + " | "

    for num3 in range(0, size):
        print(LineLong)
        print(WordLine)
        
    print(LineLong)




def run():
    print("Type a word: ")
    word = input()
    print("pick an option:")
    print("Option 1: under") 
    print("Option 2: over")
    print("Option 3: both")
    print("Option 4: grid")
    option = int(input())
    if option == 1:
        under(word)
    elif option == 2:
        over(word)
    elif option == 3:
        both(word)
    elif option == 4:
        size = int(input("what size grid? "))
        grid(word, size)
    else:
        print(ValueError)
