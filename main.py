#File Name: main.py

#Imports
from PIL import Image
import math


def hideMesssage(filename, message):

    #Local Variables

    #Array to hold edited pixel values
    pixels = []

    #index
    index = 0


    #Open image file, convert to RGB format
    im = Image.open(filename)
    
    rgb_im = im.convert('RGB')

    imgdata = list(rgb_im.getdata())

    letters = asciiToBin(message)

    for l in letters:

        r,g,b = imgdata[index]
        

        r = int("{0:08b}".format(r)[:-1] + l[0],2)
        g = int("{0:08b}".format(g)[:-1] + l[1],2)
        b = int("{0:08b}".format(b)[:-1] + l[2],2)

        im.putpixel((index,0), (r,g,b))

        pixels.append((r,g,b))

        r,g,b = imgdata[index + 1]

        r = int("{0:08b}".format(r)[:-1] + l[3],2)
        g = int("{0:08b}".format(g)[:-1] + l[4],2)
        b = int("{0:08b}".format(b)[:-1] + l[5],2)

        im.putpixel((index+1,0), (r,g,b))
        pixels.append((r,g,b))

        r,g,b = imgdata[index + 2]

        r = int("{0:08b}".format(r)[:-1] + l[6],2)
        g = int("{0:08b}".format(g)[:-1] + l[7],2)
        im.putpixel((index+2,0), (r,g,b))

        pixels.append((r,g,b))

        index = index + 3
    
    r,g,b = imgdata[2*len(letters) + len(letters)]

    #Place End of Text character at end of message
    r = int("{0:08b}".format(r)[:-1] + "0",2)
    g = int("{0:08b}".format(g)[:-1] + "0",2)
    b = int("{0:08b}".format(b)[:-1] + "0",2)
    im.putpixel((2*len(letters) + len(letters),0), (r,g,b))

    pixels.append((r,g,b))

    r,g,b = imgdata[2*len(letters) + len(letters) + 1]

    r = int("{0:08b}".format(r)[:-1] + "0",2)
    g = int("{0:08b}".format(g)[:-1] + "0",2)
    b = int("{0:08b}".format(b)[:-1] + "0",2)
    im.putpixel((2*len(letters) + len(letters) + 1,0), (r,g,b))

    pixels.append((r,g,b))

    r,g,b = imgdata[2*len(letters) + len(letters) + 2]

    r = int("{0:08b}".format(r)[:-1] + "1",2)
    g = int("{0:08b}".format(g)[:-1] + "1",2)
    im.putpixel((2*len(letters) + len(letters) + 2,0), (r,g,b))

    pixels.append((r,g,b))

    #im.putdata(pixels)

    im.save("test.png")

    im.close()

    return pixels


def showMessage(filename):

    #Local variables

    #image index
    index = 0

    #letter of message
    letter = ""

    #Message

    message = ""

     #Open image file, convert to RGB format
    im = Image.open(filename)
    
    rgb_im = im.convert("RGB")

    imgdata = list(rgb_im.getdata())

    while letter != "00000011":


        letter = ""

        r,g,b = imgdata[index]

        letter += "{0:08b}".format(r)[-1] + "{0:08b}".format(g)[-1] + "{0:08b}".format(b)[-1]

        r,g,b = imgdata[index + 1]

        letter += "{0:08b}".format(r)[-1] + "{0:08b}".format(g)[-1] + "{0:08b}".format(b)[-1]

        r,g,b = imgdata[index + 2]

        letter += "{0:08b}".format(r)[-1] + "{0:08b}".format(g)[-1]

        print(letter)

        message += chr(int(letter,2))

        index = index + 3
    
    im.close()
    
    return message




def asciiToBin(message):

    letters = []

    for letter in message:

        letters.append("{0:08b}".format(ord(letter)))
    
    return letters




#main
print(hideMesssage("test.png", "aaasdf"))
print(showMessage("test.png"))
