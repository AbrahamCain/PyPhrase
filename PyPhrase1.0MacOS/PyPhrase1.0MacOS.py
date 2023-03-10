#!/usr/bin/python
#My first attempt at a sad replacement for PhraseExpress...PyPhrase 1.0

#INSTALL/USAGE NOTE: To create a new phrase, simply place your new phrase in a .txt file
#in the "Phrases" directory naming the file with the name you'd like to type as your
#phrase. Example: if I want to type thanks to trigger my phrase, I would name the file
# thanks.txt

#NOTE TO USERS: The first three imports are native to all current (Python 3) installs,
#but the second two will take a short ammount of time to install the first time the script
#is run

#os and sys are used to run system commands to install the modules needed
import os
import sys
#time is needed for a brief pause
import time

try:
    import pyperclip
except:
    #If pyperclip is not installed, install it and then try re-importing
    os.system("/Library/Frameworks/Python.framework/Versions/3.10/bin/pip install pyperclip");import pyperclip
try:
    import keyboard
except:
    #Install the keyboard module if necessary and re-import
    os.system("/Library/Frameworks/Python.framework/Versions/3.10/bin/pip install keyboard");import keyboard


#A function to read the file to the clipboard
def copy(file):
    output=(open(file).read())
    pyperclip.copy(output)

#Allow the user to input a "Phrase" which gets turned into a filename for retrieval
filename=("Phrases/"+str(open("variablefile").read())+".txt")

#Get rid of the \n character that gets added when it echoes to the file (MacOS Bug)
filename= filename.replace("\n", "")

#Run the copy function
copy(filename)

#Change back to the previous tab and paste the data
keyboard.send("Command+tab")
keyboard.send("Command+tab")
time.sleep(1)   #A sleep timer to ensure paste happens after tab change
keyboard.send("Command+v")

#this line makes sure that no keys are hanging on
keyboard.unhook_all()
#this line sets the exit status to 0 meaning that the program finished without error
exit(0)
