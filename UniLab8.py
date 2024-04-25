# -*- coding: cp1251 -*-

from PIL import Image, ImageDraw, ImageFont

firPic = Image.open("imba.jpg")
croPic = firPic
croPic.crop((100, 75, 300, 150)).show()
croPic.save("croPIC.jpg")

picMass = {1:"passHa.jpg", 2:"novGod.jpg"}
choicePic = input("1 = Пасха, 2 = Новый год")
choicePic = int(choicePic)
secPic = Image.open(picMass[choicePic])
secPic.show()

accepter = input("Кого хотите поздравить ? ")
accepter = accepter + ", поздравляю!"
whereToWrite = {"1":(400, 100), "2":(400,700), "3":(400, 1000)}
placeToWrite = input("Где хотите расположить надпись ? 1 - Сверху, 2 - По середине, 3 - Снизу/n")
thirPic = Image.open("JAVA.jpg")
pozdravil = ImageDraw.Draw(thirPic)
writePlace = whereToWrite[placeToWrite]
fonter = ImageFont.truetype("arial.ttf", 50)
pozdravil.text(writePlace, accepter, font =fonter, size = 50)
thirPic.save("kaif.png")
