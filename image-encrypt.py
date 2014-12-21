'''
Image Encryption Program using AES-CBC

@author: Cahlen Humphreys (cahlen@gmail.com)
'''
import binascii
import Image 
import PIL
import math
from Crypto.Cipher import AES
import hashlib

# image name
imagename = "bday.jpg"

# set key, has to length of multiple 16 for AES
key = "cahlenisrad"
password = hashlib.sha256(key).digest()

# initialize variables
plaintext = list()
plaintextstr = ""

# load the image
im = Image.open(imagename)  # open target image
pix = im.load()

#print im.size   # print size of image (width,height)
width = im.size[0]
height = im.size[1]


# break up the image into a list, each with pixel values and then append to a string
for y in range(0,height):
    #print("Row: %d") %y  # print row number
    for x in range(0,width):
        #print pix[x,y]  # print each pixel RGB tuple
        plaintext.append(pix[x,y])

# add 100 to each tuple value to make sure each are 3 digits long.  being able to do this is really just a PoC 
# that you'll be able to use a raw application of RSA to encrypt, rather than PyCrypto if you wanted.
for i in range(0,len(plaintext)):
    for j in range(0,3):
        plaintextstr = plaintextstr + "%d" %(int(plaintext[i][j])+100)

# append dimensions of image for reconstruction after decryption
plaintextstr += "h" + str(height) + "h" + "w" + str(width) + "w"

# make sure that plantextstr length is a multiple of 16 for AES.  if not, append "n".  not safe in theory
# and i should probably replace this with an initialization vector IV = 16 * '\x00' at some point.  In practice
# this IV buffer should be random.
while (len(plaintextstr) % 16 != 0):
    plaintextstr = plaintextstr + "n"

# print plaintext str to a file, to large to view in console
f = open('plaintextstring', 'w')
f.write(plaintextstr)

# encrypt plaintext
obj = AES.new(password, AES.MODE_CBC, 'This is an IV456')
ciphertext = obj.encrypt(plaintextstr)

# write ciphertext to file for analysis
g = open('ciphertext', 'w')
g.write(ciphertext)

# decrypt ciphertext
obj2 = AES.new(password, AES.MODE_CBC, 'This is an IV456')
decrypted = obj2.decrypt(ciphertext)

# print to file
h = open('decrypted', 'w')
h.write(decrypted)

# parse the decrypted text back into integer string
decrypted = decrypted.replace("n","")

# extract dimensions of images
newwidth = decrypted.split("w")[1]
newheight = decrypted.split("h")[1]

# replace height and width with emptyspace in decrypted plaintext
heightr = "h" + str(newheight) + "h"
widthr = "w" + str(newwidth) + "w"
decrypted = decrypted.replace(heightr,"")
decrypted = decrypted.replace(widthr,"")

# reconstruct the list of RGB tuples from the decrypted plaintext
step = 3
finaltextone=[decrypted[i:i+step] for i in range(0, len(decrypted), step)]
finaltexttwo=[(int(finaltextone[int(i)])-100,int(finaltextone[int(i+1)])-100,int(finaltextone[int(i+2)])-100) for i in range(0, len(finaltextone), step)]    

# reconstruct image from list of pixel RGB tuples
newim = Image.new("RGB", (int(newwidth), int(newheight)))
newim.putdata(finaltexttwo)
# newim.show()

# done with the main part here

# -----------------
# construct encrypted image
# -----------------

# hexlify the ciphertext
asciicipher = binascii.hexlify(ciphertext)
#print(type(asciicipher))

# replace function
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

# use replace function to replace ascii cipher characters with numbers
reps = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23', 'x':'24', 'y':'25', 'z':'26'}
asciiciphertxt = replace_all(asciicipher, reps)

# construct encrypted image
step = 3
encimageone=[asciiciphertxt[i:i+step] for i in range(0, len(asciiciphertxt), step)]
# if the last pixel RGB value is less than 3-digits, add a digit a 1
if int(encimageone[len(encimageone)-1]) < 100:
    encimageone[len(encimageone)-1] += "1"
# check to see if we can divide the string into partitions of 3 digits.  if not, fill in with some garbage RGB values
if len(encimageone) % 3 != 0:
    while (len(encimageone) % 3 != 0):
        encimageone.append("101")

encimagetwo=[(int(encimageone[int(i)]),int(encimageone[int(i+1)]),int(encimageone[int(i+2)])) for i in range(0, len(encimageone), step)]    

# make sizes of images equal
#p = 1

while (len(finaltexttwo) != len(encimagetwo)):
    encimagetwo.pop()
    #encimagetwo = encimagetwo.pop([len(encimagetwo)-p])
    #p+=1

# encrypted image
encim = Image.new("RGB", (int(newwidth),int(newheight)))
encim.putdata(encimagetwo)

# show both images
im.show()
encim.show()
    
