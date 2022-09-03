from mysqql.connector import connect, Error

#This file sets up the MySQL database and the table that lies within the database

#todo put this into a defenition so that if needed we can call this from any other class when needed
#? Also would like to take a shower after I am done with work today so I need to let them know about that probably
#@ After I am done with them I will go back to my dorm and play some deep rock which I am really looking forward to now
try:
    with connect(
        host="localhost",
        user="goofe222",
        password="d@t@b@s3",
        databse="magic_cards"
    ) as connection:

        creatre_database_query = """"
        CREATE DATABASE magic_cards
        """
        create_table_query = """"
        CREATE TABLE cards(
            name VARCHAR(100),
            color_identity VARCHAR(100),
            type_line VARCHAR(100),
            rarity VARCHAR(100),
            frame_efects VARCHAR(100)
            expansion VARCHAR(3),
            id VARCHAR(3),
            copies int,
            price double
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(creatre_database_query)
            connection.commit()
            print("Setting up the database of magic_cards.")
            cursor.execute(create_table_query)
            print("Setting up the table cards.")
            connection.commit()


except Error as e:
    print(e)