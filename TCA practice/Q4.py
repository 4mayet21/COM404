def visit(ghost): 
   #if statement to give different reponse based on ghost
    if ghost == "Ghost of Christmas Past":
        print( "Humbug! I care not for these days of past celebration.")
    elif ghost == "Ghost of Christmas Present":
        print("Humbug! I care not for their suffering.")
    elif ghost == "Ghost of Christmas Future" :
        print("Please no more. I will change my ways. ")


# The following are calls to the function for testing purposes 
visit("Ghost of Christmas Past") 
visit("Ghost of Christmas Present") 
visit("Ghost of Christmas Future")