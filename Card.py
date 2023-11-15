import requests
import json
#@ Card class holds the data about MTG cards

#! Also need to adapt the code from MagicCardReader into the main class
class Card:
    def _init_(self, name, id, expansion, type_line, color_identity, rarity, price):
        self.name = name
        self.type_line = type_line
        self.color_identity = color_identity
        self.rarity = rarity
        self.price = price
        self.id = id
        self.expansion = expansion
        

    
    def setName(self, name):
        self.name = name
    def setTypeLine(type_line):
        self.type_line = type_line
    def setRarity(rarity):
        self.rarity = rarity
    def setPrice(price):
        self.price = price
    def setColorIdentity(color):
        self.color_identity = color_identity
    def setID(id):
        self.id = id
    def setExpansion(expansion):
        self.expansoin = expansion

    def getName(self):
        return name
    def getTypeLine(self):
        return type_line
    def getRarity(self):
        return rarity
    def getPrice(self):
        return price
    def getColorIdentity(self):
        return color_identity
    def getID(self):
        return id
    def getExpansion(self):
        return expansion

    #todo check whether this piece of code here actualy updates
    def updatePrice():
        url = "api.scryfall/cards/" + id + "/" + expansion
        oldPrice = self.price
        price = requests.get(url).json()["price"]
        print("Price went from " + oldPrice + " to " + price)
        return price
    
    def printCard():
        print(
        "Name: " + name
        + "\nID: " + id
        + "\nExpansion: " + expansion
        + "\nType_Line: " type_line
        + "\nRarity: " + rarity 
        + "\nPrice: " + price
        )