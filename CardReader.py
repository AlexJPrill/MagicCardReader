from paddleocr import *
import os

cards = os.listdir("MagicCardReader\cards")
print("Reading cards from folder")

cardPath = "Testing\cards\\"

#I realy just want to finish these parts of this program as soon as I can because this would be extremely helpful to me once this part of the program is completed in this newest version of the project

ocr = PaddleOCR(use_angle_cls=True,lang = 'en')

for card in cards:
    #This is close to the last part of this now 