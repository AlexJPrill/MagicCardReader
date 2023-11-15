#I have no idea what is going to actualy going to happen with this project now
#All I know is that I want to cleen up thi code
from supabase import create_client, Client
import os

class Supabase:

    def __init__(self):
        url = os.environ.get('SUPABASE_URL')
        key = os.environ.get('SUPABASE_KEY')
        supabase = create_client(url, key)
    

    def insertCard(self, card):
        #Insert a card into the database
        pass

    def removeCard(self, card):
        #Remove a card from the database
        pass

    def cardInDB(self, card):
        response = supabase.from_('cards').select('*').eq('card_id', card.id).eq('expansion', expansion).execute()
        if response.length == 0:
            return False
        else:
            return True


    