import sys
import os
import io
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

def encodeMessage(img, message):
	with open(img, "rb") as imageFile:
		f = imageFile.read()
		bArray = bytearray(f)

		insertBlock("", bArray)

		image = Image.open(io.BytesIO(bArray))
		image.save("img.png")

def decodeMessage(img):
	return "decode"

# Inserting block into png data
def insertBlock(block, arr):
	start = 0
	for i in range(0, len(arr)):
		# Locate index of PNG IHDR block (PNG starting block)
		if arr[i] == 73 and arr[i+1] == 72 and arr[i+2] == 68 and arr[i+3] == 82:
			start = i+4 # Start inserting at the index after IHDR block

	print arr[start]
	arr.insert(start, 3)
	arr.insert(start, 3)
	arr.insert(start, 3)
	arr.insert(start, 3)
	print arr[start], arr[start+1], arr[start+2], arr[start+3], arr[start+4]

# Takes in character, returns encoded ASCII number
def encodeChar(char):
	return ord(char)

# Takes in ASCII number, returns decoded character
def decodeChar(num):
	return chr(num)

# Only one arg, decode message
if len(sys.argv) == 2:
	print sys.argv[1] + " has the message: " + decodeMessage(sys.argv[1])		

# Two args, encode message
elif len(sys.argv) == 3:
	encodeMessage(sys.argv[1], sys.argv[2])
	print sys.argv[1] + " has been encoded with the message '" + sys.argv[2] + "'"

# Error handling
else:
	print "Usage: image:png message:string"
	print "Decoding... notage.py image"
	print "Encoding... notage.py image message"
