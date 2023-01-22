# PyPhrase

### A python replacement for PhraseExpress compatible with Windows 10 and 11, and MacOS


## How it works
It is recommended that you configure the script to be run by a hotkey combo for best results. Once propperly unzipped and setup in a hotkey, you simply use your key combo and you will be prompted for a "Phrase". After typing a phrase and hitting enter, the corresponding text file will be copied to your keyboard and pasted into the previously visited window (So not the python shell that closes right after pasting).

## How to create/edit phrases
To create a new phrase, simply create a text file in the "Phrases" directory naming it with the phrase you would like to use and ending it with a ".txt". 

For example, if I wanted to make a phrase called "thanks" that prints out "Thank you for speaking with me today", I would write "Thank you for speaking with me today" in a text file and save it with the name "thanks.txt". Then when I hit my hotkey combo, I will be prompted to enter a phrase. I will enter thanks and it will switch back to my previous window (so not the temporary python shell) and paste the full phrase contained in the thanks.txt file into my window.


## How to create a hotkey in Windows 10/11
1. Create a shortcut of the python (.py) file
  - In Windows 11
    - Right click the file
    - Click "Show more options"
    - Click "Create shortcut"
  - In Windows 10
    - Right click the file
    - Click "Create shortcut"
2. Go to the properties of the file
  - Right click the file
  - Click properties
3. Click the box next to "Shortcut Key" and enter your desired key combination. I used Ctrl+Shift+P for mine ;)
4. Click Apply and Ok to save the combo

## How to Create a hotkey in OS X (Mac OS)

1. Click the shortcut
2. Add the shortcut
3. Open the shortcut using the Apple Shortcuts tool.
4. In the top right corner of the shortcut tool, click the settings button with the three lines
5. Select the Use as Quick Action Checkbox, Services Menu, and click the Run With box
6. Enter your desired keyboard Shortcut combo
<img width="1194" alt="Screen Shot 2022-02-18 at 7 29 39 AM" src="https://user-images.githubusercontent.com/54870658/154686278-3aa0b184-1cd4-4d71-86d1-6c77e5a20a00.png">

7. Open Settings and go to Security and Privacy
8. Select Accessability on the left menu
9. Click the lock into the unlock position on the bottom right corner (May need to enter your password)
10.Check the box next to "siriactionsd" to enable it 
  a. You may have to run the shortcut once first in a notepad or somewhere that it won't mess anything up to get siriactionsd to prompt you for permission which needs to be granted in order for the Shortcut script to pass input to the python script
<img width="614" alt="Screen Shot 2022-02-18 at 7 27 58 AM" src="https://user-images.githubusercontent.com/54870658/154687086-00a7648a-dbaf-428f-a747-90b1df094d5d.png">
