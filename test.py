from paddleocr import *
import os
import requests
import json


#Need to do some basic image processing especialy on earlier cards inwhich it cannot read the bottom line of text

#todo sort out the different time periods in which cards were produce that changed the layout of the cards

cards = os.listdir("Testing\cards")
url ="https://api.scryfall.com/cards/search?unique=prints&pretty=true&q="



#What I want is for this to just work now so please just work please this should but it doesn't work now

ocr = PaddleOCR(use_angle_cls=True, lang = 'en')
for file in cards:
    result = ocr.ocr("Testing\cards\\" + file, cls = True)
    card = result[0][1][0]
    if len(card) == 1:
        card = result[1][1][0]
    print(card)





    something = url + card

    json_data = requests.get(something).json()
    variations = json_data["data"]

    for card in variations:
        match = 0

        if len(card["collector_number"]) == 1:
                collector_number = "00" + card["collector_number"]
        else:
            collector_number = card["collector_number"]

        for line in result:
            if line[1][0].count(card["set"].upper()) or line[1][0].count(card["set"]):
                print("Found Set: " + card["set"])
                match += 1
            if line[1][0].count(collector_number):
                print("Found ID: "  + card["collector_number"])
                match += 1
            if match == 2:
                break
        if match == 2:
            print("Match foudn: " + card["set_name"])
            break
    
                
    
    

    


        
    del result     
    print("---------------------------")

    





#Now I jsut need to adapt this so that it works with what I just created so lets do that now okay this should be pretty cool I think
    
    
    #This is the hard part for me so lets try our best here now okay
    






