IMEncrypt
=========

Python Image Encryption - README

AUTHOR:  Cahlen Humphreys (phku)

EMAIL:   cahlen@gmail.com

THANKS:   #blacksun on eris free, and Tilar.

DESCRIPTION:  

A simple image encryption program written completely in python.  You simply run
 the program 'python imencrypt.py' and enter your desired password to encrypt 
of decrypt the image.  After you choose your password, choose either encrypt or
 decrypt, and an file browser will show up.  From here you can choose either 
the image to encrypt, or the image to decrypt with your given password.

HOW TO RUN:

python imencrypt.py

REQUIREMENTS:

*** Python 2.7.6 or greater
*** PIL, Tkinter, PyCrypto, hashlib, binascii libraries
*** A decent computer.

COMMENTS:

12/19/2014 - Remember, I'm a mathematician, so the code could probably look
prettier.  However it runs cleanly.

12/20/2014 - The GUI could be better.  Tkinter is decent but not very pretty
to look at.  Additionally, I have incorporated an encrypted image viewer
that works, but I'm having some difficulty making it viewable pretty in the 
GUI.  It takes the encrypted file, hexifys it to ascii, removes all of the
letter characters and replaces them with random number, then reconstructs an
image using the same dimensions as the original image.  This in fact works,
so that is not the problem.  The problem is making it look pretty in the GUI.
Maybe one day I'll actually incorporate this into the GUI.

LICENSE:

The MIT License (MIT)

Copyright (c) 2014 Cahlen Humphreys 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

