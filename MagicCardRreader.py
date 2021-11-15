from mysql.connector import connect, Error
import requests
import json

#Need to edit the table to include the card id, expansion, and card_price of a single unit
#Add some error cathing for when we make the request to the scryfall api

def insert_into_table(name, color_identity, type_line, rarity, number_coppies):
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
                while i < len(result):

                    if result[i][0].replace(" ", "") == name.replace(" ", ""):
                        cursor.execute(update_number_coppies_query)
                        connection.commit()
                        print("Added " + number_coppies + " of " + name + " to the database")
                        doesExist = True
                        break
                    i = i + 1
                    
                if doesExist == False:
                    cursor.execute(insert_magic_cards_query, data)
                    print("Added " + name + " to the database")
                    connection.commit()

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
                
                cursor.execute(delete_query)
                connection.commit()
                result = cursor.fetchall()
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

def multiCard():
   f = open('cards.txt', "r")
   z = f.readlines()
   card_id = ""
   card_expansion = ""
   number_coppies = 0

   for x in range(0, len(z)):

       if "(" in z[x]:           
           index1 = z[x].find("(")+1
           index2 = z[x].find(")")
           number_coppies = z[x][index1:index2]
           split = z[x].split("/")
           card_id = split[0]
           card_expansion = split[1][0:split[1].find("(")]
       else:
            split = z[x].split("/")
            card_id = split[0]
            card_expansion = split[1][0:len(split[1])]
            number_coppies = 1

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















