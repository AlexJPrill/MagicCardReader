from mysqql.connector import connect, Error
try:
    with connect(
        host="localhost",
        user="goofe222",
        password="d@t@b@s3",
        databse="magic_cards"
    ) as connection:
        create_table_query = """"
        CREATE TABLE cards(
            name VARCHAR(100),
            color_identity VARCHAR(100),
            type_line VARCHAR(100),
            rarity VARCHAR(100),
            expansion VARCHAR(3),
            id VARCHAR(3),
            copies int,
            price double
        )
        """
        with connection.cursor() as cursor:
            print("Setting up the table")


except Error as e:
    print(e)