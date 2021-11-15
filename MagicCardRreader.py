from mysql.connector import connect, Error
import requests
import json

#First version almost done just need to add in the price to the data
#Then need to do some cleaning up of the code and getting rid of things that I dont need

#Want to add in a feature that will allow the user to paste a bunch of cards into a file and the program will go in and add in all of the cards

def insert_into_table(name, color_identity, type_line, rarity, number_coppies):
    #print(name)
    try:
        with connect(
            host="localhost",
            user="goofe222",
            password="d@t@b@s3",
            database="magic_cards"
        ) as connection:
            data = (name, color_identity, type_line, rarity, number_coppies)
            insert_magic_cards_query = """
            INSERT INTO cards(name, color_identity, type_line, rarity, number_coppies)
            VALUES(%s, %s, %s, %s, %s)
        """


            
            #Select all cards in the table
            select_cards_query = "SELECT * FROM cards"

            card_update = (int(number_coppies), name)
            update_number_coppies_query = """
            UPDATE
                cards
            SET
                number_coppies = number_coppies + "%s"
            WHERE
                name = "%s"
            """ % (number_coppies, name)

            delete_query = """
            DELETE FROM cards WHERE name = "Sol Ring"
            """

            
            with connection.cursor() as cursor:
                cursor.execute(select_cards_query)
                result = cursor.fetchall()
                
                
                
                
                i = 0
                doesExist = False
                #Need to find another way to check to see if the names match up 
                while i < len(result):
                    

                    if result[i][0].replace(" ", "") == name.replace(" ", ""):
                        cursor.execute(update_number_coppies_query)
                        connection.commit()
                        doesExist = True
                        break
                    i = i + 1
                    
                if doesExist == False:
                    cursor.execute(insert_magic_cards_query, data)
                    print("Added additional card to database")
                    connection.commit()

                connection.commit()
                result = cursor.fetchall()
                connection.commit()
    except Error as e:
        print(e)


def selectAll(name, color_identity, type_line, rarity, number_coppies):
    try:
        with connect(
            host="localhost",
            user="goofe222",
            password="d@t@b@s3",
            database="magic_cards"
        ) as connection:
        
            data = (name, type_line, rarity, 12)
            insert_magic_cards_query = """
            INSERT INTO cards(name, color_identity, type_line, rarity, number_coppies)
            VALUES(%s, "Green", %s, %s, %s)
        """
            
            insert_magic_cardz = """"
            INSERT INTO cardz (name, rarity)
            VALUES (%s, %s)
            """

            show_table_query = "DESCRIBE cards"
            select_cards_query = "SELECT * FROM cards"
            create_table_cardz_query = """
            CREATE TABLE cardz(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                color_identity VARCHAR(100),
                type_line VARCHAR(100),
                rarity VARCHAR(100),
                number_coppies INT
            )
            """

            card_update = name
            update_number_coppies_query = """
            UPDATE
                cards
            SET
                number_coppies = number_coppies + 1
            WHERE
                name = %s
            """ 

            delete_query = """
            truncate table cards
            """

            
            with connection.cursor() as cursor:
                cursor.execute(select_cards_query)
                result = cursor.fetchall()
                print(len(result))
                for x in result:
                    print(x)
                
                cursor.execute(delete_query)
                connection.commit()
                result = cursor.fetchall()
                for x in result:
                    print(x)
                    print("Hello")
                connection.commit()
    except Error as e:
        print(e)



def singleCard():
    url = "https://api.scryfall.com/cards/"
    card_id = input("Please enter the cards id:")
    card_expansion = input("Please enter the cards expasion: ")
    url += card_expansion + "/" + card_id
    response = requests.get(url)
    json_data = response.json()
    card_name = json_data["name"]
    card_rarity = json_data["rarity"]
    card_type_line = json_data["type_line"]
    card_color_identity = json_data["color_identity"]

    color_identity = ""
    for x in card_color_identity:
        if x == "G":
            color_identity += "Green"
        elif x == "B":
            color_identity += "Black"
        elif x == "U":
            color_identity += "Blue"
        elif x == "W":
            color_identity += "White"
        elif x == "R":
            color_identity += "Red"
        else:
            color_identity += "Colorless"
    number_coppies = 1
    insert_into_table(card_name, color_identity, card_type_line, card_rarity, number_coppies)




#need to change this now very badly
def multiCard():

   f = open('cards.txt', "r")
   z = f.readlines()
   card_id = ""
   card_expansion = ""

   for x in range(0, len(z)-1):
       
       if "(" in z[x]:
           index1 = z[x].find("(")+1
           index2 = z[x].find(")")-1
           number_coppies = z[x][index1:index2]
           split = z[x].split("/")
           card_id = split[0]
           card_expansion = z[x][4:7]
       else:
           split = z[x].split("/")
           card_id = split[0]
           card_expansion = split[1][0:3]
       url = "https://api.scryfall.com/cards/"
       #need to change this now very badly
def multiCard():
   f = open('cards.txt', "r")
   z = f.readlines()
   card_id = ""
   card_expansion = ""
   number_coppies = 0

   for x in range(0, len(z)):
       print(z[x])
       print("(" in z[x])
       if "(" in z[x]:
           print("This works now")
           
           index1 = z[x].find("(")+1
           index2 = z[x].find(")")
           number_coppies = z[x][index1:index2]
           split = z[x].split("/")
           card_id = split[0]
           card_expansion = split[1][0:split[1].find("(")]
           print(number_coppies)
       else:
            split = z[x].split("/")
            card_id = split[0]
            card_expansion = split[1][0:len(split[1])]
            number_coppies = 1
            #print(card_expansion)

       print(number_coppies)
       url = "https://api.scryfall.com/cards/"
       url += card_expansion + "/" + card_id
       print(url)
       response = requests.get(url)
       json_data = response.json()
       card_name = json_data["name"]
       card_rarity = json_data["rarity"]
       card_type_line = json_data["type_line"]
       card_color_identity = json_data["color_identity"]
       color_identity = ""
       for x in card_color_identity:

           if x == "G":
                color_identity += "Green"
           elif x == "B":
                color_identity += "Black"
           elif x == "U":
                color_identity += "Blue"
           elif x == "W":
                color_identity += "White"
           elif x == "R":
                color_identity += "Red"
           else:
                color_identity += "Colorless"
            
           
       #print(card_name)

       insert_into_table(card_name, color_identity, card_type_line, card_rarity, number_coppies)



loop = True
while loop == True:
    print("Welcome to the magic card read er program please select an option")
    print("0)exit program")
    print("1)Enter in single card")
    print("2)Add cards in bulk from file")
    userInput = input()
    if userInput == "0":
        quit()
    elif userInput == "1":
        singleCard()
    elif userInput == "2":
        print("Please make sure that the file is populated with the correct cards that you would like to have added to the data base")
        multiCard()
    else:
        print("Sorry that was not a valid option")














#print(data[0])
#Why is the sql unable process the parameters could it please give me some more valuable information instead of the very vague decription that they gave me
#selectAll(card_name, card_color_identity, card_type_line, card_rarity, 12)

#Hey this is a change to the repositor