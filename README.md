#PyPhrase
###A python replacement for PhraseExpress compatible with Windows 10 and 11 (OS X is pending Testing)


##How it works
It is recommended that you configure the script to be run by a hotkey combo for best results. Once propperly unzipped and setup in a hotkey, you simply use your key combo and you will be prompted for a "Phrase". After typing a phrase and hitting enter, the corresponding text file will be copied to your keyboard and pasted into the previously visited window (So not the python shell that closes right after pasting).

##How to create/edit phrases
To create a new phrase, simply create a text file in the "Phrases" directory naming it with the phrase you would like to use and ending it with a ".txt". 

For example, if I wanted to make a phrase called "thanks" that prints out "Thank you for speaking with me today", I would write "Thank you for speaking with me today" in a text file and save it with the name "thanks.txt". Then when I hit my hotkey combo, I will be prompted to enter a phrase. I will enter thanks and it will switch back to my previous window (so not the temporary python shell) and paste the full phrase contained in the thanks.txt file into my window.


##How to create a hotkey in Windows 10/11
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

##How to Create a hotkey in OS X (Mac OS)
On your Mac, choose Apple menu  > System Preferences, click Keyboard , then click Shortcuts.

1. In the list on the left, select a category, such as Mission Control or Spotlight.
2. In the list on the right, select the checkbox next to the shortcut that you want to change.
3. Double-click the current key combination, then press the new key combination you want to use.
4. You can’t use each type of key (for example, a letter key) more than once in a key combination.
5. Quit and reopen any apps you’re using for the new keyboard shortcut to take effect.
  - If you assign a keyboard shortcut that already exists for another command or app, your new shortcut won’t work. Find the menu command that’s using it, then reassign the keyboard shortcut for that item.
  - If you want to return all the shortcuts to their original keystroke combinations, go to the Shortcuts pane of Keyboard preferences and click Restore Defaults.
