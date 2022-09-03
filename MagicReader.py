from mysql.connector import connect, Error
import requests
import json

#Need to edit the table to include the card_id, expansion, and card_price of a single unit
#Add some error cathing for when we make the request to the scryfall api



#Takes the given values and adds them to the table
#todod Add functionality to remove a given listing from the table if its value reaches zero or a negative value
#todo If the value becomes below zero print some sort of error message to the console and remove it from the table
#todo May want to make the argument a card object would simplify everything and make it more readable
#todo Would like to clean up this code and try to fit as much as I can into other methods to thus try and clean up this code
def insert_into_table(name, color_identity, type_line, rarity, number_coppies):
    try:

        #? Would it be possible to take this code here and put it into its own method
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


            #!Why does this even work here
            #!Need to test to make sure if this works
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

            #Need to put a query in here to delete a card from the table

            with connection.cursor() as cursor:
                cursor.execute(select_cards_query)
                result = cursor.fetchall()
                
                
                
                
                i = 0
                doesExist = False
                while i < len(result):
                    # result[i][0] is the name and the method is just checking to see if they match
                    #todo Need to add logic to check if the number of copies will be less than or equal to zero if so then delete entry from the table 
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





#Takes user input and either updates existing rows or creates new ones
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

    color_identity = colorIdentity(card_color_identity)
    number_coppies = 1
    insert_into_table(card_name, color_identity, card_type_line, card_rarity, number_coppies)




#Takes inputs from a text document and either updates existing row or creates new ones
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
       color_identity = colorIdentity(card_color_identity)
            
       insert_into_table(card_name, color_identity, card_type_line, card_rarity, number_coppies)


def colorIdentity(colors):
    color_identity = ""
    for x in colors:
        
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

    return color_identity

















