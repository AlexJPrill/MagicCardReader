from MagicReader import *
#Yay we fixed it now for the most part I think now to fix all the indentation that I may or may not have messed up at some point so lets go fix that now please


#Main part of the program
print("Welcome to the magic card read er program please select an option")

#@ Do we want to use this style of window for the program or do we want to try to do something else
while True:
    print("0)exit program")
    #Oh that was just a really bad error on my part so then everything should be working properly I think so I will have to double check that when I can
    print("1)Enter in single card")
    print("2)Add cards in bulk from file")
    print("3)Remove any amount of a specified card")
    userInput = input()
    if userInput == "0":
        quit()
    elif userInput == "1":
        singleCard()
    elif userInput == "2":
        print("Please make sure that the file is populated with the correct cards that you would like to have added to the database")
        multiCard()
    elif userInput == "3":
        #Thats why I am such an idiot for not noticing that so lets fix that pronto right now
        removeCard()
    elif userInput == "4":
        print("Going to take cards from images")
    else:
        print("Sorry that is not a valid option")