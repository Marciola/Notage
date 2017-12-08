import sys
from PIL import Image, ImageFile

def encodeMessage(img, message):
    originalImage = Image.open(img)
    pixels = list(originalImage.getdata())

    pixels = insertMessage(pixels, message)

    newImage = Image.new(originalImage.mode, originalImage.size)
    newImage.putdata(pixels)
    newImage.save("example.png" ,originalImage.format)

def decodeMessage(img):
    count = 0
    message = ""

    originalImage = Image.open(img)
    pixels = list(originalImage.getdata())

    while pixels[count + 1] != 2 and pixels[count + 2] != 0 \
    and pixels[count + 3] != 1 and pixels[count + 4] != 7:
        message += decodeChar(pixels[count])
        count += 1

    print(message)

def insertMessage(pixels, message):
    messageLength = len(message)
    pixelsLength = len(pixels)
    count = 0

    while count < messageLength and count < (pixelsLength-4):
        pixels[count] = encodeChar(message[count])
        count += 1

    pixels[count+1] = 2
    pixels[count+2] = 0
    pixels[count+3] = 1
    pixels[count+4] = 7

    return pixels

# Takes in character, returns encoded ASCII number
def encodeChar(char):
    return ord(char)

# Takes in ASCII number, returns decoded character
def decodeChar(num):
    return chr(num)


# Only one arg, decode message
#if len(sys.argv) == 2:
 #   print sys.argv[1] + " has the message: " + decodeMessage(sys.argv[1])

# Two args, encode message
#elif len(sys.argv) == 3:
 #   print "Encoding..."
  #  encodeMessage(sys.argv[1], sys.argv[2])
   # print sys.argv[1] + " has been encoded with the message '" + sys.argv[2] + "'"



# Error handling
"""else:
    print "Usage: image:png message:string"
    print "Decoding... notage.py image"
    print "Encoding... notage.py image message"
"""
