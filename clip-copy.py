#This script copies the file to your clipboard
import pyperclip

filename="Phrases/pc.txt"

def paste(filename):
    output=(open(filename).read())
    pyperclip.copy(output)
