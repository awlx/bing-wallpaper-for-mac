# bing-wallpaper-for-mac
Bing wallpaper for mac

This program is written in python specifically for OSX and tested on High Sierra running python 2.7.9 and 3.4.3

### Notes

-  The app calls the python scripts on execution.
-  In order to save space, the script keeps *only 1 image* in the ~/Pictures/bing-wallpaper folder.
-  Place all the files into a single folder. Here it is in the Applications folder within the user's home directory - `~/Applications/Bing Wallpaper`
-  Open the plist file with your favorite editor and change the username to your username

![Image](http://i.imgur.com/Zr9qkQs.jpg)

### The App
- The wallpaper downloader app ensures that you only have the latest wallpaper in your folder. It makes sure to delete all files from that folder before downloading the new wallpaper.
- It also restarts your Dock so all Desktops get the new background image

### Plist File
- Copy the plist file to `~/Library/LaunchAgents`
```
cp bing.wallpaper.mac.plist ~/Library/LaunchAgents
```
- Edit the plist file to reflect your username
- Save and close
- Run the following terminal command
```
launchctl load ~/Library/LaunchAgents/bing.wallpaper.mac.plist
```

### Uninstall
- To uninstall run this command
```
launchctl unload ~/Library/LaunchAgents/bing.wallpaper.mac.plist
```
- Delete the `~/Applications/Bing Wallpaper` folder and its contents
- Delete the `~/Pictures/bing-wallpaper` folder and its contents

###Thanks
Feel free to share your comments and thoughts.
